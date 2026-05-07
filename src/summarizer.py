import os
import anthropic
from dotenv import load_dotenv

load_dotenv()

def summarize_transcript(transcript: str) -> str:
    """Send transcript to Claude and return a structured summary."""
    client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

    message = client.messages.create(
        model="claude-opus-4-5",
        max_tokens=1024,
        messages=[
            {
                "role": "user",
                "content": (
                    "Please summarize the following video transcript. "
                    "Include:\n"
                    "- A brief overview (2-3 sentences)\n"
                    "- Key points (bullet list)\n"
                    "- Main takeaways\n\n"
                    f"Transcript:\n{transcript}"
                ),
            }
        ],
    )

    return message.content[0].text
