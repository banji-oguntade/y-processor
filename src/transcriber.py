from pathlib import Path
import whisper

def transcribe_audio(audio_path: Path, model_size: str = "base") -> str:
    """Transcribe an audio file using OpenAI Whisper."""
    model = whisper.load_model(model_size)
    result = model.transcribe(str(audio_path))
    return result["text"].strip()
