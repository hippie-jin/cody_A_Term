import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()


def generate_brand_story(brief: dict) -> str:
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("[스토리 생성 실패] OPENAI_API_KEY가 설정되지 않았습니다. .env 파일을 확인하세요.")
        return ""

    prompt = f"""아래 브랜드 브리프를 바탕으로 브랜드 스토리를 작성해줘.

- 업종: {brief.get("industry", "")}
- 타겟: {brief.get("target", "")}
- 키워드: {", ".join(brief.get("keywords", []))}
- 톤앤매너: {brief.get("tone", "")}
- 브랜드 퍼스널리티: {brief.get("brand_personality", "")}
- 타겟의 페인포인트: {", ".join(brief.get("pain_points", []))}
- 주 사용 순간: {brief.get("usage_moment", "")}
- 참고 메모: {brief.get("notes", "")}

조건:
- 브랜드의 탄생 배경, 철학, 비전을 포함할 것
- 타겟의 페인포인트에 공감하며 시작할 것
- 분량은 한글 기준 300자 내외
- 문체는 브리프의 톤앤매너를 따를 것
- 스토리 본문만 출력하고, 제목이나 설명은 붙이지 말 것"""

    try:
        client = OpenAI(api_key=api_key)
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "너는 브랜드 스토리텔링 전문 카피라이터야."},
                {"role": "user", "content": prompt},
            ],
            temperature=0.8,
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"[스토리 생성 실패] {e}")
        return ""


if __name__ == "__main__":
    import json

    with open("brief.json", encoding="utf-8") as f:
        sample_brief = json.load(f)

    story = generate_brand_story(sample_brief)
    print(f"생성된 스토리 ({len(story)}자):\n{story}")
