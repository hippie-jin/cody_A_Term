# 브랜드 아이덴티티 생성기 (Term Project A)

대전 코디세이 AI 활용 실습 Term Project. 브랜드 브리프를 입력하면 LLM API와
이미지 생성 API로 네이밍·슬로건·스토리·컬러·로고 시안을 자동 생성하는 CLI 프로그램.

## 팀 구성 (5인)

| 역할 | 담당 업무 | 파일 |
|---|---|---|
| 팀장 | 일정관리, brief.json 확정, 최종 취합 | - |
| 텍스트 담당 | 네이밍 3~5개 + 슬로건 3개 | `naming.py` |
| 콘텐츠 담당 | 브랜드 스토리 + 컬러 팔레트 | `content.py` |
| 비주얼 담당 | 컬러 시각화 + 로고 시안 생성 | `visual.py` |
| 통합·보안 담당 | API 키 관리, CLI, 결과 통합 | `main.py` |

## 파이프라인

브리프 입력(JSON) → AI 텍스트 생성(네이밍·슬로건·스토리·컬러) → AI 이미지 생성(로고) → 결과 저장(JSON+PNG)

## 개발 순서

1. **함께 설계**: `brief.example.json`을 참고해 팀 브랜드 컨셉을 확정하고 `brief.json`으로 저장 (git에는 커밋하지 않고 팀 내부 공유 또는 각자 로컬 보관)
2. **각자 개발**: 담당 파일에서 함수 구현
3. **각자 테스트**: 담당 파일 단독 실행
4. **중간 통합**: `main.py`에서 함수 연결
5. **전체 테스트**: 새 `brief.json`으로 처음부터 끝까지 실행

## 환경 설정

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env  # 이후 .env에 실제 API 키 입력
```

## 결과물 (`output/`)

- `brand_result.json` - 네이밍·슬로건·스토리·컬러 텍스트 결과
- `color_palette.png` - 컬러 팔레트 시각화
- `logo_01.png`, `logo_02.png` - 로고 시안
