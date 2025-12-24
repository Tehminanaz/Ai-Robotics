# Personalization and Translation API Endpoints

This document describes the new API endpoints for content personalization and translation added to the Robotics course platform.

## Personalization Endpoint

The personalization endpoint allows tailoring course content based on the user's background.

### Endpoint
`POST /api/v1/personalization/personalize`

### Request Body
```json
{
  "content": "string - The original chapter content to personalize",
  "user_background": "string - Information about the user's background, knowledge level, field of expertise, etc.",
  "chapter_title": "string - (Optional) The title of the chapter for context"
}
```

### Response
```json
{
  "personalized_content": "string - The content personalized for the user's background"
}
```

### Example Request
```json
{
  "content": "Robots are machines that can perform tasks automatically. They are widely used in manufacturing and research.",
  "user_background": "I am a computer science student with knowledge of programming but new to robotics.",
  "chapter_title": "Introduction to Robotics"
}
```

## Translation Endpoint

The translation endpoint allows translating content to different languages, including Urdu.

### Endpoint
`POST /api/v1/personalization/translate`

### Request Body
```json
{
  "content": "string - The content to translate",
  "target_language": "string - The target language code (default: 'ur' for Urdu)"
}
```

### Supported Languages
- `ur` - Urdu (default)
- `es` - Spanish
- `fr` - French
- `de` - German
- `zh` - Chinese
- `hi` - Hindi
- `ar` - Arabic

### Response
```json
{
  "translated_content": "string - The translated content"
}
```

### Example Request
```json
{
  "content": "Robots are machines that can perform tasks automatically.",
  "target_language": "ur"
}
```

## Implementation Details

Both endpoints use OpenAI's GPT-4o model for:
1. Personalization: Adapting content to match the user's background, experience level, and interests
2. Translation: Converting content to target languages while preserving technical meaning

The endpoints require the `OPENAI_API_KEY` environment variable to be set for production use.

## Integration

These endpoints are integrated into the existing FastAPI application and can be accessed alongside other API endpoints at `/api/v1/`.