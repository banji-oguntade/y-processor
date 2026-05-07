# YouTube Transcript & Summary Pipeline

A modular Python CLI tool that automates the process of extracting, transcribing, and summarizing content from YouTube videos. 

## 🚀 Features

- **Download:** Fetches the highest quality video and audio from any YouTube URL using `yt-dlp`.
- **Extract:** Converts the downloaded video into an MP3 audio file using `moviepy`.
- **Transcribe:** Generates a highly accurate text transcript using the local `openai-whisper` model.
- **Summarize:** Creates a structured, concise summary of the transcript using the Anthropic API (Claude).
- **Export:** Saves the full transcript and generated summary into a clean text file.

## 📋 Prerequisites

Before running the application, ensure you have the following:

- **Python 3.8+** installed on your system.
- An **Anthropic API Key** (to generate the summary).
- *(Note: Transcription runs locally via Whisper, so no OpenAI API key is required).*

## 🛠️ Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/banji-oguntade/youtube-pipeline.git
   cd youtube-pipeline
   ```

2. **Install the dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up Environment Variables:**
   Create a `.env` file in the root directory and add your Anthropic API key:
   ```env
   ANTHROPIC_API_KEY=your_anthropic_api_key_here
   ```

## 💻 Usage

Run the pipeline by passing a YouTube URL to `main.py`:

```bash
python main.py "https://www.youtube.com/watch?v=YOUR_VIDEO_ID"
```

### Output

The pipeline will create the following directories and files:
- `video/` - Stores the downloaded raw MP4 video.
- `audio/` - Stores the extracted MP3 audio file.
- `transcripts/` - Stores the final output `.txt` file containing the full transcript and the generated summary.

## 📁 Project Structure

```
youtube-pipeline/
├── main.py              # CLI Entry point
├── requirements.txt     # Python dependencies
├── .env                 # Environment variables (API keys)
├── .gitignore           # Git ignore rules
└── src/                 # Core pipeline modules
    ├── downloader.py    # Handles YouTube downloads (yt-dlp)
    ├── extractor.py     # Handles audio extraction (moviepy)
    ├── transcriber.py   # Handles speech-to-text (Whisper)
    └── summarizer.py    # Handles summarization (Anthropic API)
```
