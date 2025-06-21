#!/usr/bin/env python3
"""
Example usage of the voice-to-text CLI tool
"""

import subprocess
import sys
from pathlib import Path


def main():
    """Example demonstrating how to use the CLI tool."""

    # Get the current directory
    current_dir = Path(__file__).parent

    print("🎤 Voice to Text CLI Example")
    print("=" * 40)

    # Show help
    print("\n📖 Showing help:")
    try:
        result = subprocess.run(
            [sys.executable, "-m", "src.main", "--help"],
            cwd=current_dir,
            capture_output=True,
            text=True,
        )
        print(result.stdout)
    except Exception as e:
        print(f"Error showing help: {e}")

    # Example commands (commented out since we don't have actual audio files)
    print("\n📝 Example usage commands:")
    print("# Basic usage:")
    print("uv run python -m src.main audio_file.m4a")
    print()
    print("# With specific model:")
    print("uv run python -m src.main --model large audio_file.m4a")
    print()
    print("# Save to file:")
    print("uv run python -m src.main --output transcription.txt audio_file.m4a")
    print()
    print("# Combined options:")
    print("uv run python -m src.main --model medium --output result.txt audio_file.m4a")

    print("\n✨ CLI tool is ready to use!")
    print("📁 Place your m4a files in this directory and run the commands above.")


if __name__ == "__main__":
    main()
