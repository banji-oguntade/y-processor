import argparse
from src.downloader import download_video
from src.extractor import extract_audio
from src.transcriber import transcribe_audio
from src.summarizer import summarize_transcript

def run_pipeline(url: str):
    print(f"\n🎬 Starting pipeline for: {url}\n")

    # Step 1: Download video
    video_path = download_video(url, output_dir="video")
    print(f"✅ Video saved to: {video_path}")

    # Step 2: Extract audio
    audio_path = extract_audio(video_path, output_dir="audio")
    print(f"✅ Audio saved to: {audio_path}")

    # Step 3: Transcribe audio
    transcript = transcribe_audio(audio_path)
    print(f"✅ Transcription complete ({len(transcript.split())} words)")

    # Step 4: Summarize transcript
    summary = summarize_transcript(transcript)
    print(f"✅ Summary generated")

    # Step 5: Save output
    base_name = video_path.stem
    output_path = f"transcripts/{base_name}.txt"
    with open(output_path, "w") as f:
        f.write("=== TRANSCRIPT ===\n\n")
        f.write(transcript)
        f.write("\n\n=== SUMMARY ===\n\n")
        f.write(summary)

    print(f"\n📄 Output saved to: {output_path}\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="YouTube Video Pipeline")
    parser.add_argument("url", help="YouTube video URL")
    args = parser.parse_args()
    run_pipeline(args.url)
