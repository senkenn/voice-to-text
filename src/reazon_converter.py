import os
from reazonspeech.k2.asr import load_model, transcribe, audio_from_path


class ReazonSpeechConverter:
    def __init__(self, model_name="reazonspeech-k2-v2"):
        """
        Initialize ReazonSpeech converter.

        Args:
            model_name (str): ReazonSpeech model name
        """
        self.model_name = model_name
        self.model = None
        self._load_model()

    def _load_model(self):
        """Load the ReazonSpeech model."""
        try:
            self.model = load_model()
        except Exception as e:
            raise Exception(
                f"Failed to load ReazonSpeech model '{self.model_name}': {str(e)}"
            )

    def convert_to_text(self, audio_file, language="ja"):
        """
        Convert audio file to text using ReazonSpeech.

        Args:
            audio_file (str): Path to the audio file
            language (str): Language code (currently only 'ja' is supported)

        Returns:
            str: Transcribed text
        """
        if not os.path.exists(audio_file):
            raise FileNotFoundError(f"Audio file not found: {audio_file}")

        if self.model is None:
            raise Exception("ReazonSpeech model not loaded")

        try:
            # Load audio using ReazonSpeech's audio loader
            audio = audio_from_path(audio_file)

            # Transcribe using ReazonSpeech
            ret = transcribe(self.model, audio)

            return ret.text.strip()

        except Exception as e:
            raise Exception(f"Failed to transcribe audio: {str(e)}")
