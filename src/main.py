import click
import os
from pathlib import Path
from .whisper_converter import WhisperConverter
from .reazon_converter import ReazonSpeechConverter


@click.command()
@click.argument("file_path", type=click.Path(exists=True))
@click.option(
    "--model",
    default="base",
    help="Model to use: Whisper (tiny, base, small, medium, large) or ReazonSpeech (reazon)",
)
@click.option("--output", "-o", help="Output file path (optional)")
@click.option(
    "--language",
    "-l",
    default="ja",
    help="Language code (e.g., ja for Japanese, en for English). Defaults to Japanese (ja).",
)
def main(file_path, model, output, language):
    """Convert an audio file to text using Whisper or ReazonSpeech."""
    if not os.path.exists(file_path):
        click.echo(f"Error: File '{file_path}' not found.", err=True)
        return

    # Check file extension
    file_path = Path(file_path)
    if file_path.suffix.lower() not in [".m4a", ".mp3", ".wav", ".mp4"]:
        click.echo(
            f"Warning: File extension '{file_path.suffix}' may not be supported.",
            err=True,
        )

    try:
        # Choose converter based on model
        if model == "reazon":
            click.echo("Loading ReazonSpeech model...")
            converter = ReazonSpeechConverter()
        else:
            click.echo(f"Loading Whisper model '{model}'...")
            converter = WhisperConverter(model_name=model)

        click.echo(f"Converting '{file_path}' to text (language: {language})...")
        text = converter.convert_to_text(str(file_path), language=language)

        if output:
            with open(output, "w", encoding="utf-8") as f:
                f.write(text)
            click.echo(f"Text saved to '{output}'")
        else:
            click.echo("\n--- Transcribed Text ---")
            click.echo(text)

    except Exception as e:
        click.echo(f"Error: {str(e)}", err=True)


if __name__ == "__main__":
    main()
