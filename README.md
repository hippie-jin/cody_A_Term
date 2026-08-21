# 브랜드 아이덴티티 생성기 (Term Project A)

대전 코디세이 AI 활용 실습 Term Project. 브랜드 브리프를 입력하면 LLM API와
이미지 생성 API로 네이밍·슬로건·스토리·컬러·로고 시안을 자동 생성하는 CLI 프로그램.

## 팀 구성 (6인)

| 담당자 | 파트 | 담당 업무 | 파일 |
|---|---|---|---|
| 최우성 | 메인 & 입출력 | 터미널 경로 입력, brief.json 로드, 결과 취합해 brand_result.json 저장 | `main.py` |
| 박세훈 | 네이밍 | LLM API로 브랜드 이름 후보 3~5개 + 의미 생성 | `naming.py` |
| 윤혜민 | 슬로건 | LLM API로 톤앤매너에 맞는 슬로건 3개 생성 | `slogan.py` |
| 전황진 | 스토리 | LLM API로 300자 내외 브랜드 탄생 스토리 생성 | `story.py` |
| 박효령 | 컬러 팔레트 | LLM으로 메인/서브 컬러 HEX 추출 + matplotlib으로 color_palette.png 저장 | `color.py` |
| 임동혁 | 로고 생성 | 이미지 생성 API로 로고 시안 2~3개 생성 후 PNG 저장 | `logo.py` |

## 파이프라인

브리프 입력(JSON) → AI 텍스트 생성(네이밍·슬로건·스토리·컬러) → AI 이미지 생성(로고) → 결과 저장(JSON+PNG)

## 개발 순서

1. **함께 설계**: `brief.json`의 입력 필드와 각 모듈의 출력(JSON) 형식을 먼저 합의
2. **각자 개발**: 담당 파일에서 자신의 모듈 함수 구현
3. **각자 테스트**: 담당 파일을 단독 실행해 정상 동작 확인
4. **취합**: 최우성이 각자의 모듈을 `main.py`에서 하나씩 연결
5. **전체 테스트**: `brief.json`으로 처음부터 끝까지 실행해 `output/` 결과물 확인

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
