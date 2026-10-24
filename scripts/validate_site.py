#!/usr/bin/env python3
"""공개 정책 사이트의 파일·metadata·링크·리소스를 표준 라이브러리로 검증한다."""

from datetime import date
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
errors = []


def fail(path, message):
    errors.append(f"{path.relative_to(ROOT)}: {message}")


def metadata(path):
    text = path.read_text(encoding="utf-8")
    match = re.match(r"\A---\s*\n(.*?)\n---\s*\n", text, re.S)
    if not match:
        fail(path, "frontmatter가 없습니다.")
        return {}, text
    values = {}
    for key, value in re.findall(r"^([\w_]+):\s*(.*?)\s*$", match[1], re.M):
        if key in values:
            fail(path, f"metadata key가 중복됩니다: {key}")
        values[key] = value.strip("\"'")
    return values, text[match.end():]


required = ["_config.yml", "_layouts/default.html", "_layouts/policy.html",
            "assets/style.css", "index.md", "404.html", "site-privacy/index.md", "nudge/index.md",
            "nudge/terms/index.md", "nudge/privacy/index.md", "nudge/history/index.md"]
for name in required:
    if not (DOCS / name).is_file():
        fail(DOCS / name, "필수 파일이 없습니다.")

config_path = DOCS / "_config.yml"
if config_path.is_file():
    config = config_path.read_text(encoding="utf-8")
    for key, expected in [("url", "https://newrecord-team.github.io"),
                          ("baseurl", "/service-policies")]:
        match = re.search(rf"^{key}:\s*[\"']?([^\s\"']+)", config, re.M)
        if not match or match[1] != expected:
            fail(config_path, f"{key}는 {expected}이어야 합니다.")
    if re.search(r"^(?:theme|remote_theme|plugins)\s*:", config, re.M):
        fail(config_path, "추가 theme 또는 plugin은 사용하지 않습니다.")
if (DOCS / "CNAME").exists():
    fail(DOCS / "CNAME", "Custom domain 설정은 사용하지 않습니다.")

pages = {}
page_sources = {}
for path in sorted(DOCS.rglob("*")):
    if not path.is_file() or path.suffix not in {".md", ".html", ".css"}:
        continue
    text = path.read_text(encoding="utf-8")
    if re.search(r"<script\b|<iframe\b|@import\b|@font-face\b", text, re.I):
        fail(path, "script, iframe, 외부 import 또는 font 선언을 사용할 수 없습니다.")
    if re.search(r'(?:src|href)\s*=\s*["\'](?:https?:)?//[^"\']+\.(?:js|css|woff2?)(?:[?"\'])', text, re.I):
        fail(path, "외부 실행·스타일·font 리소스가 있습니다.")
    if re.search(r"\b(?:TODO|TBD|FIXME|PLACEHOLDER)\b|example\.com|추후\s*작성|작성\s*예정", text, re.I):
        fail(path, "미완성 placeholder가 있습니다.")
    if "_layouts" in path.parts or path.suffix == ".css":
        continue
    values, body = metadata(path)
    for field in ("layout", "title", "permalink"):
        if not values.get(field):
            fail(path, f"{field} metadata가 필요합니다.")
    permalink = values.get("permalink", "")
    if not permalink.startswith("/") or permalink.startswith("/service-policies"):
        fail(path, "permalink는 baseurl을 제외한 / 경로여야 합니다.")
    if permalink in pages:
        fail(path, f"permalink가 중복됩니다: {permalink}")
    pages[permalink] = path
    page_sources[path] = (values, body)
    if values.get("layout") == "policy":
        for field in ("service", "version", "published_date", "effective_date"):
            if not values.get(field):
                fail(path, f"정책의 {field} metadata가 필요합니다.")
        if not re.fullmatch(r"\d+\.\d+\.\d+", values.get("version", "")):
            fail(path, "정책 버전은 숫자 세 자리 형식이어야 합니다.")
        for field in ("published_date", "effective_date"):
            try:
                date.fromisoformat(values.get(field, ""))
            except ValueError:
                fail(path, f"{field}는 유효한 YYYY-MM-DD여야 합니다.")
        if "/archive/" in permalink and not values.get("current_url"):
            fail(path, "보관본에는 current_url이 필요합니다.")
        if "/archive/" not in permalink and values.get("current_url"):
            fail(path, "현재 정책에는 current_url을 지정하지 않습니다.")

for path in sorted(DOCS.rglob("*")):
    if not path.is_file() or path.suffix not in {".md", ".html"}:
        continue
    text = path.read_text(encoding="utf-8")
    for target in re.findall(r"{{\s*['\"]([^'\"]+)['\"]\s*\|\s*relative_url\s*}}", text):
        destination = target.split("#", 1)[0]
        if destination not in pages and not (DOCS / destination.lstrip("/")).is_file():
            fail(path, f"내부 링크 대상이 없습니다: {target}")
    if re.search(r'(?:href|src)=["\']/(?!/)|\]\(/', text):
        fail(path, "절대 내부 링크에는 relative_url을 사용해야 합니다.")
    for expression in re.findall(r"{{(.*?)}}", text, re.S):
        if re.match(r"\s*['\"]/", expression) and "relative_url" not in expression:
            fail(path, "Liquid 내부 경로에 relative_url이 누락되었습니다.")

for path, (values, body) in page_sources.items():
    current_url = values.get("current_url")
    if current_url and current_url not in pages:
        fail(path, f"현재 정책 링크 대상이 없습니다: {current_url}")

privacy = DOCS / "nudge/privacy/index.md"
if privacy.is_file() and not re.search(r'(?:id=["\']website-visits["\']|\{:\s*#website-visits\s*\})', privacy.read_text(encoding="utf-8")):
    fail(privacy, "웹사이트 방문 안내의 website-visits anchor가 필요합니다.")

if errors:
    print("정책 사이트 검증 실패:", file=sys.stderr)
    for error in errors:
        print(f"- {error}", file=sys.stderr)
    sys.exit(1)
print(f"정책 사이트 검증 성공: {len(pages)}개 페이지의 metadata·내부 링크·리소스를 확인했습니다.")
