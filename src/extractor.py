from pathlib import Path
from moviepy import VideoFileClip

def extract_audio(video_path: Path, output_dir: str = "audio") -> Path:
    """Extract audio from a video file and save as .mp3."""
    Path(output_dir).mkdir(exist_ok=True)

    audio_path = Path(output_dir) / (video_path.stem + ".mp3")

    clip = VideoFileClip(str(video_path))
    clip.audio.write_audiofile(str(audio_path), logger=None)
    clip.close()

    return audio_path
