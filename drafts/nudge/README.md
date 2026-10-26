# Nudge 개인정보처리방침 1.2.0 검수 메모

- 검수 기준일: 2026-10-25
- 전체 초안: [privacy-1.2.0.md](privacy-1.2.0.md)
- 상태: 출시용 Crashlytics·Google Analytics 사용 방향을 반영한 **비공개 경로의 검수 자료**. Git 저장소에 올리면 저장소 공개 여부에 따라 보일 수 있으나 Pages의 `docs` 게시 대상에는 포함되지 않는다.
- 공개 중인 1.1.0, 약관, 변경 이력, 사이트 설정은 수정하지 않았다. 초안 작성은 SDK 설정 변경·production 전송·게시·시행 승인이나 법률 적합성 확인이 아니다.
- 게시일·시행일 미정. 기존 1.1.0의 기기 내 정보·Apple·이메일·웹사이트·권리 안내를 유지하고 서두·§4·§7을 주로 수정했다. 새 본문은 출시 시 적용하려는 정책이며 현재 production 콘솔 설정을 확인했다는 뜻이 아니다.

## 확인된 범위

소스 기준은 Nudge의 `issue-74-store-style` checkout과 `docs/firebase-data-policy-v1.md`, custom 사건 사전 및 탐색 담당자의 소스 대조다. Firebase Apple SDK 13.0.0 / GoogleAppMeasurement 13.0.1을 기준으로 한다. SDK 내부 payload 재추출·실기기 전송 재검증은 하지 않았다.

- 앱의 맞춤 사건은 Pro 7종 + 집중 잠금 4종이다. SDK 자동 수집·자동 구매/구독 사건은 별도로 고지한다.
- `FirebaseAnalyticsCore`를 사용하며 광고 IdentitySupport는 연결하지 않는다. IDFV·자동 화면 조회 수집을 끄고 광고 관련 consent를 denied로 설정한다. 나머지 자동 사건을 모두 끈다는 의미는 아니다.
- Crashlytics 맞춤 log/key/user ID/nonfatal API 호출은 없다. SDK 자체의 진단·식별자 및 Analytics breadcrumb가 없다는 의미는 아니다.
- App Store 수집 공개안에서 app instance ID로 연결되는 분석은 계정이 없다는 이유로 비연결 처리하지 않는다. SDK manifest 자체만으로 전체 앱 공개 답변을 확정하지 않는다.
- 승인 정책: 기본 ON·사용자용 OFF Toggle 없음, Analytics 사용자/이벤트 14개월·새 활동 시 사용자 데이터 갱신 ON, Crashlytics 90일 후 삭제 개시. dev/prod 분리·Spark·Ads/signals/별도 export 미사용을 유지한다.
- 생활 기록·앱 목록·Screen Time 토큰·야식/수면 설정·잠금 기간/이력·영수증/JWS·직접 개인식별 정보를 분석 사건으로 보내지 않는다. SDK 사건 시각·대략적 지역·설치 식별자·통신 메타데이터는 별도로 존재할 수 있다.

## 맞춤 사건 대조표

근거: Nudge `docs/issue-26-analytics-measurement-plan.md`, `docs/issue-69-focus-lock-analytics.md` 및 현재 구현의 허용 payload. 원문에는 이용자가 읽을 수 있는 의미로 반영한다.

| 사건 | 의미 |
| --- | --- |
| `pro_offer_first` | Pro 첫 안내 노출 |
| `pro_purchase_first` | 첫 구매 시작 |
| `pro_trial_started` | 체험 시작 |
| `pro_paid_observed` | 확인된 유료 결제 |
| `pro_purchase_result` | 구매 결과 |
| `pro_restore_result` | 복원 결과 |
| `pro_paid_revoked` | 유료 거래 철회 관찰 |
| `focus_setup_opened` | 집중 잠금 설정 표시 |
| `focus_start_requested` | 수락한 시작 요청 |
| `focus_start_result` | 등록 결과 |
| `focus_pro_requested` | 명시적인 Pro 안내 진입 |

Pro 공통 값은 `schema_version=s2`, `offer_version=o1`, `store_env=production|sandbox|simulation|unknown`이며 체험 자격은 값이 있을 때 `eligible|ineligible`이다. 첫 구매·체험 시작·결제 관찰·철회 사건에 `plan=monthly|annual`, 구매 결과에는 plan과 result, 복원 결과에는 result를 허용한다. 집중 잠금 공통 값은 `focus_schema_version=f1`, `source=live|simulation`이며 시작 결과에만 `result=registered|failed`를 더한다. 유입 경로·선택 앱·앱 수·잠금 기간 등 이 사전에 없는 값을 추가로 수집한다고 쓰지 않는다.

## App Privacy의 연결 여부 판단

SDK별 manifest의 linked=false를 Analytics와 결합한 최종 앱의 연결 여부로 그대로 확대하지 않는다. Analytics의 설치 식별자, Crashlytics breadcrumb 및 Analytics의 자동 app_exception 연동을 고려해 검수안은 6개 유형 모두 사용자와 연결됨으로 보수적으로 작성한다. 개별 Crashlytics 보고서의 모든 필드가 실명과 연결된다고 주장하는 것은 아니다. 충돌 데이터에는 Analytics의 안정성 분석 목적도 포함한다. 기타 진단도 Analytics의 앱/기기 상태·오류 사건과 설치 단위 연결을 포함한다. SDK 표준 계약을 대조한 판단이며 새로운 payload 실험을 요구하지 않는다.

외부 고객지원 이메일이 App Privacy의 앱 수집에 해당하는지는 기존 미확정 경계를 유지한다. 별도 이메일 처리는 방침에 고지하며, Firebase 사용 결정만으로 이메일 신고 분류를 확정하지 않는다.

## 공개 전 확정해야 하는 운영 정보

다음은 초안 본문에서 완료된 사실처럼 쓰지 않은 사항이다. 이 목록을 숨긴 채 전체 초안을 곧바로 공개하면 국외이전·거부/철회 안내가 불완전하다.

| 항목 | 남은 결정·확인 및 본문 반영 |
| --- | --- |
| 수집과 국외이전의 적용 근거 | 실제 서비스 계약과 대상 시장을 기준으로 처리 근거와 개인정보 보호법 제28조의8 적용 근거를 확정한다. 비동의 처리나 계약 이행 필요성을 임의로 선언하지 않는다. |
| 이전 국가·수령인 연락처 | Google LLC의 계약상 수령 주체·공식 연락처 및 실제 적용 서비스의 이전 국가 고지 정보를 확보한다. 글로벌 시설이라는 설명만으로 국가 목록 고지를 완료 처리하지 않는다. Firebase의 미국 전용 Authentication 설명은 Crashlytics/Analytics에 적용하지 않는다. |
| 거부·동의 철회 방식과 효과 | 기본 ON·별도 Toggle 없음이라는 제품 결정은 유지하되, 필요한 동의/철회 및 국외이전 거부 절차·실제 효과를 #32에서 확정하여 §4에 추가한다. 앱 삭제·문의 이메일·정책 게시만으로 적합성 충족이라고 쓰지 않는다. 아직 구현되지 않은 OFF 기능도 안내하지 않는다. |
| Analytics 삭제 요청 | 요청자를 확인하고 현재 app instance ID와 삭제 대상을 안전하게 연결하는 방법, 권한 있는 운영자의 공식 삭제 요청, 처리 확인·실패 대응을 확정한다. 식별자를 먼저 초기화하여 과거 대상을 잃지 않도록 한다. 사용자 입력만으로 타인의 자료를 삭제하지 않는다. |
| Crashlytics 삭제 요청 | 설치 단위 서버 삭제 가능 경로·지원 채널·대상 식별과 처리 기한을 확인한다. user ID 제거·기기 삭제·90일 경과가 즉시 완전 삭제라는 안내는 금지한다. |
| 콘솔 설정과 담당자 | production Analytics 보관 14개월·reset ON, Ads/signals·export·서비스 데이터 공유 설정 및 실제 dev/prod 경계, 관리자/MFA·운영 책임자를 확인한다. 현재 값과 승인 정책을 혼동하지 않는다. |
| 서비스 운영 데이터 | Google 자체 서비스 운영 정보의 계약·처리 범위와 보관 고지를 검토한다. Crashlytics 고객 데이터 90일이나 GA 원본 14개월을 모든 운영·통신 정보에 적용하지 않는다. |
| 게시·시행과 출시 연결 | 위 내용을 반영한 최종 문서의 게시·시행일, 현재 정책 교체 및 1.1.0 보관·이력 반영을 별도 승인받는다. App Privacy 답변·앱 고지·실제 production 활성화가 같은 출시 구성과 일치해야 한다. |

§4의 외부 처리 표에는 확인된 사업자·항목·목적·전송 시점과 방식·보관만 채웠다. 국가·법적 근거·거부 절차/효과·공급자 연락처·개별 삭제 경로는 위 운영 정보가 확정되면 보완한다. 이것은 최종 공개 가능 판정이 아니다.

## 공식 근거

2026-10-25 읽기 확인 기준이다. 공급자 공식 설명과 실제 앱 설정을 대조했으며, 표준 SDK 전체를 다시 시험하지 않았다.

- [Firebase 개인정보·보안](https://firebase.google.com/support/privacy): Crashlytics 식별자·진단 및 90일 후 운영/백업 삭제 개시, 글로벌 처리 시설, Google 서비스 운영 데이터, Analytics의 별도 조건.
- [Firebase Apple 플랫폼 수집 공개](https://firebase.google.com/docs/ios/app-store-data-collection): Crashlytics 진단·Analytics 연계 breadcrumb와 실제 앱 사용에 따른 공개 책임.
- [Google Analytics App Store 공개 안내](https://support.google.com/analytics/answer/10285841): app instance ID, 마스킹된 IP 기반 대략 지역, StoreKit 구매/구독, lifecycle/session 자동 수집.
- [Google Analytics 자동 사건](https://support.google.com/analytics/answer/9234069): Crashlytics 연동 시 app_exception과 fatal·발생 시각 등의 사건, SDK 오류 사건을 포함한다.
- [Google Analytics 보관 설정](https://support.google.com/analytics/answer/7667196): 사용자·이벤트 보관과 활동 시 사용자 보관기간 갱신, 표준 집계와의 구분. 14개월·ON 선택은 Nudge PO 정책이며 production 설정 실측은 아니다.
- [개인정보 보호법 제28조의8](https://www.law.go.kr/LSW/lsLinkCommonInfo.do?chrClsCd=010202&lsJoLnkSeq=1029331957): 적용 근거와 이전 항목·국가·시기/방법·수령자/연락처·목적/보유기간·거부 절차와 효과에 관한 고지 확인. 특정 근거가 Nudge에 적용된다는 법률 판단은 하지 않았다.
- [Apple App Review 개인정보 기준](https://developer.apple.com/app-store/review/guidelines/#privacy): 기존 #32의 동의·철회 적합성 gate에서 대조할 기준. 출시 사용 결정이 해당 gate 완료를 뜻하지 않는다.

## 검수 범위와 결과

기존 공개 1.1.0의 §1·§2·§3·§5·§6·§8 본문 원문 유지를 확인했다. 신규 파일 2개는 `git diff --no-index --check /dev/null <파일>`로 공백 오류 없이 통과했다. 사건 범위·보관/삭제 구분도 대조했다. `drafts/`만 변경하므로 사이트 구조 검사·앱 build·기기 테스트는 반복하지 않는다. 실제 국외이전 계약·콘솔 설정·삭제 운영 확인은 아직 하지 않았으며 앞선 정책 게시 성공 증거로 대신하지 않는다.
