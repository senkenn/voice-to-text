#!/usr/bin/env python3

import sys
import os

sys.path.append("/home/senken/senkenn/voice-to-text/src")

from reazon_converter import ReazonSpeechConverter


def test_reazon():
    audio_file = "tmp.m4a"
    print(f"Testing ReazonSpeech with {audio_file}")

    try:
        converter = ReazonSpeechConverter()
        print("Model loaded successfully!")

        text = converter.convert_to_text(audio_file)
        print(f"Transcription: {text}")

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    test_reazon()
