import asyncio
import json
from backend.api.personalization import personalize_content, translate_content
from backend.api.personalization import PersonalizeRequest, TranslateRequest

async def test_personalization():
    print("Testing Personalization API...")

    # Test personalization
    personalize_req = PersonalizeRequest(
        content="Robots are machines that can perform tasks automatically. They are widely used in manufacturing and research.",
        user_background="I am a computer science student with knowledge of programming but new to robotics.",
        chapter_title="Introduction to Robotics"
    )

    result = await personalize_content(personalize_req)
    print("Personalization result:", result.personalized_content[:200] + "..." if len(result.personalized_content) > 200 else result.personalized_content)
    print()

async def test_translation():
    print("Testing Translation API...")

    # Test translation to Urdu
    translate_req = TranslateRequest(
        content="Robots are machines that can perform tasks automatically. They are widely used in manufacturing and research.",
        target_language="ur"
    )

    result = await translate_content(translate_req)
    print("Translation result:", result.translated_content[:200] + "..." if len(result.translated_content) > 200 else result.translated_content)
    print()

async def main():
    await test_personalization()
    await test_translation()

if __name__ == "__main__":
    asyncio.run(main())