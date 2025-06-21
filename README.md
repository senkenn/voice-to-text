# Voice to Text Converter

A CLI tool to convert audio files to text using both OpenAI Whisper and ReazonSpeech models.

## Features

- **Multiple Model Support**: Choose between OpenAI Whisper and ReazonSpeech models
- **Audio Format Support**: m4a, mp3, wav, mp4 files
- **Whisper Models**: tiny, base, small, medium, large
- **ReazonSpeech**: Optimized for Japanese speech recognition
- **Output Options**: Display results or save to file
- **Language Support**: Automatic detection or specify language

## Installation

```bash
# Install dependencies using uv
uv sync
```

## Usage

### Basic Usage

```bash
# Using Whisper (default base model)
uv run python -m src.main audio_file.m4a

# Using ReazonSpeech (optimized for Japanese)
uv run python -m src.main --model reazon audio_file.m4a
```

### Advanced Usage

```bash
# Specify Whisper model size
uv run python -m src.main --model large audio_file.m4a

# Save output to file
uv run python -m src.main --model reazon --output result.txt audio_file.m4a

# Specify language (for Whisper)
uv run python -m src.main --model base --language en audio_file.m4a
```

## Model Comparison

### Whisper Models

- **tiny**: Fastest, least accurate (~39 MB)
- **base**: Good balance of speed and accuracy (~74 MB)
- **small**: Better accuracy (~244 MB)
- **medium**: High accuracy (~769 MB)
- **large**: Best accuracy (~1550 MB)

### ReazonSpeech

- **Optimized for Japanese**: Specifically trained on Japanese audio data
- **Fast Processing**: Efficient inference with good accuracy
- **Japanese Focus**: Better performance on Japanese speech compared to general models

## Example Results

With `tmp.m4a` (Japanese audio):

- **ReazonSpeech**: "よろしくお願いし"
- **Whisper**: Similar results but may vary in accuracy for Japanese

## Dependencies

- openai-whisper
- reazonspeech-k2-asr
- click
- torch
- torchaudio
- transformers
- librosa

## Requirements

- Python >= 3.12
- CUDA GPU (recommended, but CPU also works)
