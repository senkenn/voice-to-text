#!/usr/bin/env python3

"""
Simple test script to compare Whisper and ReazonSpeech models
"""

import sys
import os
sys.path.append('src')

from whisper_converter import WhisperConverter
from reazon_converter import ReazonSpeechConverter

def test_models(audio_file):
    print(f"Testing with audio file: {audio_file}")
    print("=" * 50)
    
    # Test Whisper
    print("Testing Whisper (base model)...")
    try:
        whisper_conv = WhisperConverter("base")
        whisper_result = whisper_conv.convert_to_text(audio_file, language="ja")
        print(f"Whisper result: {whisper_result}")
    except Exception as e:
        print(f"Whisper error: {e}")
    
    print()
    
    # Test ReazonSpeech
    print("Testing ReazonSpeech...")
    try:
        reazon_conv = ReazonSpeechConverter()
        reazon_result = reazon_conv.convert_to_text(audio_file, language="ja")
        print(f"ReazonSpeech result: {reazon_result}")
    except Exception as e:
        print(f"ReazonSpeech error: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python test_comparison.py <audio_file>")
        sys.exit(1)
    
    audio_file = sys.argv[1]
    if not os.path.exists(audio_file):
        print(f"Error: Audio file '{audio_file}' not found.")
        sys.exit(1)
    
    test_models(audio_file)
