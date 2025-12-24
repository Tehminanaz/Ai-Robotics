from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
import os

router = APIRouter(prefix="/personalization", tags=["personalization"])

class PersonalizeRequest(BaseModel):
    content: str
    user_background: str
    chapter_title: Optional[str] = ""

class TranslateRequest(BaseModel):
    content: str
    target_language: str = "ur"  # Default to Urdu

class PersonalizeResponse(BaseModel):
    personalized_content: str

class TranslateResponse(BaseModel):
    translated_content: str

@router.post("/personalize", response_model=PersonalizeResponse)
async def personalize_content(request: PersonalizeRequest):
    """
    Personalize chapter content based on user's background
    """
    try:
        llm = ChatOpenAI(
            model_name=os.getenv("OPENAI_MODEL_NAME", "gpt-4o"),
            temperature=0.3
        )

        prompt_template = """You are an educational content personalizer. Your task is to adapt the given chapter content to better suit the background and needs of a specific learner.

Original Content: {content}

User's Background: {user_background}

Chapter Title: {chapter_title}

Please rewrite the content to make it more relevant and engaging for this user. Consider:
- Using examples and analogies that relate to their background
- Adjusting the complexity level based on their experience
- Highlighting aspects that would be most relevant to their interests or field
- Maintaining the core educational value while making it more accessible to them

Personalized Content:"""

        PROMPT = PromptTemplate(
            template=prompt_template,
            input_variables=["content", "user_background", "chapter_title"]
        )

        chain = PROMPT | llm
        response = await chain.ainvoke({
            "content": request.content,
            "user_background": request.user_background,
            "chapter_title": request.chapter_title
        })

        return PersonalizeResponse(personalized_content=response.content)

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Personalization failed: {str(e)}")


@router.post("/translate", response_model=TranslateResponse)
async def translate_content(request: TranslateRequest):
    """
    Translate content to the specified language (default Urdu)
    """
    try:
        llm = ChatOpenAI(
            model_name=os.getenv("OPENAI_MODEL_NAME", "gpt-4o"),
            temperature=0.1
        )

        # Define language names for better context
        language_names = {
            "ur": "Urdu",
            "es": "Spanish",
            "fr": "French",
            "de": "German",
            "zh": "Chinese",
            "hi": "Hindi",
            "ar": "Arabic"
        }

        target_language_name = language_names.get(request.target_language, request.target_language)

        prompt_template = """You are a professional translator. Translate the following content to {target_language}.
Maintain the educational context, technical terms, and meaning accurately.
If there are technical terms that don't have direct translations, keep them in the original language but provide context.

Content to translate:
{content}

Translation in {target_language_name}:"""

        PROMPT = PromptTemplate(
            template=prompt_template,
            input_variables=["target_language", "content", "target_language_name"]
        )

        chain = PROMPT | llm
        response = await chain.ainvoke({
            "target_language": request.target_language,
            "content": request.content,
            "target_language_name": target_language_name
        })

        return TranslateResponse(translated_content=response.content)

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Translation failed: {str(e)}")