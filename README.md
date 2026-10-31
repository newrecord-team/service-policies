# 돌돌소프트 정책 센터

돌돌소프트 서비스의 공개 이용약관과 개인정보처리방침을 관리합니다. 현재 등록된 서비스는 Nudge입니다. 운영자는 돌돌소프트, 대표자는 신기록이며 공개 문의 주소는 `latency.sprint@gmail.com`입니다.

## 공개 주소와 배포

- 정책 센터: https://newrecord-team.github.io/service-policies/
- 정책 사이트 개인정보 안내: https://newrecord-team.github.io/service-policies/site-privacy/
- Nudge 정책: https://newrecord-team.github.io/service-policies/nudge/
- 이용약관: https://newrecord-team.github.io/service-policies/nudge/terms/
- 개인정보처리방침: https://newrecord-team.github.io/service-policies/nudge/privacy/
- 고객지원: https://newrecord-team.github.io/service-policies/nudge/support/
- 변경 이력: https://newrecord-team.github.io/service-policies/nudge/history/

GitHub repository `newrecord-team/service-policies`의 Pages 설정에서 **Deploy from a branch → main → /docs**를 선택합니다. GitHub Pages의 기본 Jekyll build를 사용하며 별도 theme, plugin, framework, custom workflow는 사용하지 않습니다. Custom domain은 설정하지 않습니다. `_config.yml`의 `url`과 `baseurl`을 유지하고 내부 링크에는 `relative_url`을 적용합니다.

앱·스토어·외부 문서에서 사용하는 현재 정책 주소는 개정 후에도 바꾸지 않습니다. 게시 완료 여부는 설정 저장과 별개로 Pages build 결과와 공개 URL의 응답으로 확인합니다.

## 구성

`docs/index.md`는 서비스 목록, `docs/<서비스>/index.md`는 서비스별 정책 안내입니다. 현재 정책은 `terms/index.md`와 `privacy/index.md`, 변경 이력은 `history/index.md`에 둡니다. 공통 layout과 스타일은 `docs/_layouts/` 및 `docs/assets/style.css`에서 관리합니다.

JavaScript, 분석 도구, 쿠키 설정 코드, 외부 font를 포함하지 않습니다. 서비스가 처리하는 개인정보와 이 웹사이트의 GitHub Pages 보안 기록은 구분합니다. 사이트 자체의 방문·문의 안내는 `docs/site-privacy/index.md`에서 관리하고 공통 footer에서 연결합니다.

## 새 서비스 추가

1. 공개 URL에서 계속 사용할 고유한 영문 slug를 정하고 `docs/<slug>/` 아래에 안내, 이용약관, 개인정보처리방침, 변경 이력 페이지를 만듭니다.
2. 각 페이지에 고유한 `permalink`를 지정합니다. 정책에는 `layout: policy`, `title`, `service`, `service_slug`, `version`, `published_date`, `effective_date`, `permalink`를 작성합니다. `service_slug`는 표시 이름과 URL이 다른 서비스에 필수이며, 생략하면 서비스 이름의 Jekyll `slugify` 값을 사용합니다.
3. 정책 센터의 서비스 목록에 실제 공개할 서비스만 추가하고, 공통 layout을 재사용합니다. 서비스별 운영 사실과 개인정보 처리 내용을 확인한 뒤 문서를 작성합니다.
4. 검증 도구와 게시 후 링크 확인 절차를 실행합니다.

## 정책 개정

1. 현재 본문과 metadata를 `docs/<slug>/archive/<type>/<version>.md`에 그대로 복사합니다. `<type>`은 `terms` 또는 `privacy`입니다.
2. 보관본의 `permalink`만 `/<slug>/archive/<type>/<version>/`로 변경하고 `current_url: /<slug>/<type>/`를 추가합니다. 이전 게시일·시행일·버전·본문은 유지합니다. 보관본은 이후 수정하지 않습니다.
3. 현재 정책의 내용·버전·게시일·시행일을 갱신합니다. `current_url`은 현재 정책에는 넣지 않습니다. 현재 정책의 `permalink`는 유지합니다.
4. 변경 이력에 개정 요약, 게시일, 시행일, 버전 및 보관본 링크를 추가합니다. 기존 이력의 이전 버전 링크도 해당 보관본을 가리키게 합니다.
5. 현재 정책, 보관본, 변경 이력을 **같은 commit**에서 변경합니다. 보관본을 포함한 내부 링크와 목차가 여전히 올바른지 확인합니다.

정책을 개정해도 과거 문서가 현재 버전을 가리키지 않도록 버전별 링크를 점검합니다. 소급 적용 여부나 중요한 정책 변경은 실제 운영 조건과 함께 별도로 검토합니다.

## Nudge 운영 사실 확인

개인정보처리방침 1.2.0은 선택 동의 후 Firebase 분석·충돌 보고를 사용하는 출시 구성에 맞춘 게시 후보입니다. 현재 로컬 준비 상태이며 원격 게시 성공·Release 수집 활성화를 뜻하지 않습니다. 정책 게시와 앱 배포를 구분합니다.

2026-10-25 개정한 Nudge 정책 1.1.0은 표시 이름·월간/연간 자동 갱신 구독·집중 잠금과 관련 기기 내 정보 처리를 반영합니다. 1.0.0 원문은 버전별 보관본에 유지하며, App Store 지원 URL로 사용할 정적 고객지원 페이지를 제공합니다. 출시 완료나 production 수집 활성화를 뜻하지 않습니다.

### 실제 운영 전 확인

- Nudge 유료 판매·체험의 제공 여부와 실제 판매 조건이 앱·Apple 구매 화면 및 약관의 안내와 일치하는지 확인합니다.
- 고객지원은 공개된 Gmail 주소를 사용합니다. Google이 안내한 국외 처리 가능성을 문서에 설명했지만, 그 설명만으로 국내 개인정보보호법상 국외이전 근거와 국가·수령인 연락처·보관기간 등 고지 요건의 충족을 확정한 것은 아닙니다. 실제 이메일 서비스 계약·처리 흐름과 필요한 절차를 확인해 문서에 반영합니다. 일반 문의의 삭제 절차도 운영에서 이행해야 합니다.
- App Store에 필요한 사업자·판매자 정보는 별도로 실제 등록 정보와 맞춥니다. 공개 정책 저장소에 사업자등록증 원본·생년월일·인증정보를 올리지 않습니다.
- 문서의 기술적 동작 대조와 게시 성공은 법률 적합성, 앱 심사 통과 또는 출시 승인을 대신하지 않습니다.

## 검증 방법

Repository root에서 다음 명령을 실행합니다. Python 표준 라이브러리만 필요합니다.

```sh
python3 scripts/validate_site.py
```

필수 파일, URL 설정, 정책 metadata, 중복 permalink, 내부 링크, placeholder, 외부 실행·font 리소스가 올바르면 종료 코드 `0`과 성공 메시지를 출력합니다. 정적 소스 검증이므로 Jekyll의 실제 render나 법률 검토를 대신하지 않습니다.

게시 전후에는 다음을 확인합니다.

- GitHub Pages build가 성공했는지 확인합니다.
- 공개 root, Nudge 안내, 이용약관, 개인정보처리방침, 변경 이력과 존재하지 않는 주소의 404 화면을 엽니다.
- 작은 화면에서 본문·표·이메일이 잘리지 않고, Tab 키로 링크와 본문 바로가기에 접근할 수 있는지 확인합니다.
- 정책 날짜·버전과 목차, 웹사이트 방문 안내 링크가 정확한지 확인합니다.
- 인쇄 미리보기에서 본문과 metadata가 읽기 좋게 표시되는지 확인합니다.
- 개정 시 보관본의 이전 버전 안내와 현재 정책 링크를 확인합니다.
