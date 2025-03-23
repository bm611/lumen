import os
import json
import logging
from google import genai
from typing import Dict, List
from pydantic import BaseModel


# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


# Define Pydantic models for structured story data
class Chapter(BaseModel):
    chapter_number: int
    chapter_name: str
    text: str
    image: str


class Story(BaseModel):
    title: str
    chapters: List[Chapter]


# Initialize the Gemini client
def get_gemini_client():
    """Get a configured Gemini API client."""
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        logger.error("GEMINI_API_KEY environment variable is not set")
        raise ValueError("GEMINI_API_KEY environment variable is not set")
    return genai.Client(api_key=api_key)


def generate_story(theme: str) -> Dict:
    """Generate a complete story with chapters and image prompts based on a theme.

    Args:
        theme: The theme or topic for the story

    Returns:
        A dictionary containing the story title and chapters
    """
    logger.info(f"Generating story with theme: {theme}")

    try:
        client = get_gemini_client()
        logger.info("Gemini client initialized successfully")

        prompt = f"""Generate a children's story about {theme}.
The story should have a creative title and exactly 3 chapters.
Each chapter should have a chapter number (1, 2, or 3), an interesting name, 
engaging text content appropriate for children (50-100 words), and a simple image prompt for a 3D cartoon image.
Make sure each chapter's text contains dialogue and is age-appropriate.
For the image prompts, keep them simple and concise, suitable for 3D cartoon style.
"""

        logger.info("Sending request to Gemini API with structured output")
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt,
            config={
                "response_mime_type": "application/json",
                "response_schema": Story,
                "max_output_tokens": 8192,
                "temperature": 2,
            },
        )

        # Use the parsed response directly
        try:
            story_data = response.parsed
            logger.info(
                f"Successfully parsed structured story response with title: {story_data.title}"
            )

            # Convert Pydantic model to dictionary
            return story_data.model_dump()

        except Exception as parse_error:
            logger.error(f"Error parsing structured response: {parse_error}")

            # Fallback to text parsing if structured parsing fails
            logger.warning("Falling back to text response parsing")
            story_json = response.text

            try:
                # Try to parse as JSON
                story_dict = json.loads(story_json)
                logger.info("Successfully parsed JSON from text response")

                # Validate with Pydantic model
                story_data = Story(**story_dict)
                return story_data.model_dump()

            except Exception as json_error:
                logger.error(f"Error parsing JSON from text: {json_error}")
                raise ValueError(f"Failed to parse story data: {json_error}")

    except Exception as e:
        logger.error(f"Error generating story: {e}", exc_info=True)
        # Return a fallback story in case of API errors
        logger.info(f"Returning fallback story for theme: {theme}")
        return {
            "title": f"Adventure in {theme.title()} Land",
            "chapters": [
                {
                    "chapter_number": 1,
                    "chapter_name": "The Beginning",
                    "text": "Once upon a time in a magical world, a young explorer named Sam discovered a map to the mysterious "
                    + f'{theme} Land. "Look at this!" Sam exclaimed to his friend Lily. "We could go on a real adventure!" '
                    + "Lily's eyes widened with excitement. \"Let's do it!\" she replied. Together, they packed their bags and set off on what would become the journey of a lifetime.",
                    "image": f"A 3D cartoon of two children looking at a magical map showing {theme} Land, with glowing elements and soft lighting.",
                },
                {
                    "chapter_number": 2,
                    "chapter_name": "The Challenge",
                    "text": f"As Sam and Lily ventured deeper into {theme} Land, they encountered a massive river blocking their path. "
                    + '"How will we cross?" worried Sam. Lily spotted some large stepping stones. "We can use those!" she pointed. '
                    + '"But they look slippery," Sam hesitated. "We\'ll go together," Lily reassured him, taking his hand. '
                    + "Step by careful step, they helped each other across the challenging obstacle.",
                    "image": f"A 3D cartoon of children carefully crossing stepping stones over a sparkling river in {theme} Land, helping each other.",
                },
                {
                    "chapter_number": 3,
                    "chapter_name": "The Discovery",
                    "text": f"Finally reaching their destination, Sam and Lily gasped at the beautiful {theme} treasure before them. "
                    + '"It\'s even better than I imagined!" Sam whispered in awe. "And we found it together," smiled Lily. '
                    + 'As the sun began to set, they knew it was time to return home. "We\'ll come back someday," promised Sam. '
                    + 'Lily nodded happily. "This will always be our special adventure." Hand in hand, they headed home, their hearts full of memories.',
                    "image": f"A 3D cartoon of two children discovering a magical {theme} treasure that glows with soft, colorful light in a beautiful landscape at sunset.",
                },
            ],
        }


# Example usage (commented out for production)
if __name__ == "__main__":
    theme = "space exploration"
    story = generate_story(theme)

    # Print the story structure
    print(f"Story Title: {story['title']}\n")

    # Print each key
    print("Story keys:")
    for key in story.keys():
        print(f"- {key}")

    # Print chapters
    print("\nChapters:")
    for i, chapter in enumerate(story["chapters"]):
        print(f"\nCHAPTER {chapter['chapter_number']}: {chapter['chapter_name']}")
        print(f"Image prompt: {chapter['image']}")
        print(f"Text: {chapter['text'][:100]}...")

        # Only print keys for the first chapter
        if i == 0:
            print("\nChapter keys:")
            for key in chapter.keys():
                print(f"- {key}")
