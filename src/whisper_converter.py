import whisper
import os


class WhisperConverter:
    def __init__(self, model_name="base"):
        """
        Initialize Whisper converter with specified model.

        Args:
            model_name (str): Whisper model size ('tiny', 'base', 'small', 'medium', 'large')
        """
        self.model_name = model_name
        self.model = None
        self._load_model()

    def _load_model(self):
        """Load the Whisper model."""
        try:
            self.model = whisper.load_model(self.model_name)
        except Exception as e:
            raise Exception(
                f"Failed to load Whisper model '{self.model_name}': {str(e)}"
            )

    def convert_to_text(self, audio_file, language=None):
        """
        Convert audio file to text using Whisper.

        Args:
            audio_file (str): Path to the audio file
            language (str, optional): Language code (e.g., 'ja', 'en'). Auto-detect if None.

        Returns:
            str: Transcribed text
        """
        if not os.path.exists(audio_file):
            raise FileNotFoundError(f"Audio file not found: {audio_file}")

        if self.model is None:
            raise Exception("Whisper model not loaded")

        try:
            result = self.model.transcribe(audio_file, language=language)
            return result["text"].strip()
        except Exception as e:
            raise Exception(f"Failed to transcribe audio: {str(e)}")
