import pytest
from unittest.mock import Mock, patch
from src.whisper_converter import WhisperConverter


class TestWhisperConverter:
    """Test cases for WhisperConverter class."""

    @patch("src.whisper_converter.whisper.load_model")
    def test_init_default_model(self, mock_load_model):
        """Test initialization with default model."""
        mock_model = Mock()
        mock_load_model.return_value = mock_model

        converter = WhisperConverter()

        assert converter.model_name == "base"
        assert converter.model == mock_model
        mock_load_model.assert_called_once_with("base")

    @patch("src.whisper_converter.whisper.load_model")
    def test_init_custom_model(self, mock_load_model):
        """Test initialization with custom model."""
        mock_model = Mock()
        mock_load_model.return_value = mock_model

        converter = WhisperConverter(model_name="large")

        assert converter.model_name == "large"
        assert converter.model == mock_model
        mock_load_model.assert_called_once_with("large")

    @patch("src.whisper_converter.whisper.load_model")
    def test_init_model_load_failure(self, mock_load_model):
        """Test model loading failure."""
        mock_load_model.side_effect = Exception("Model load failed")

        with pytest.raises(
            Exception, match="Failed to load Whisper model 'base': Model load failed"
        ):
            WhisperConverter()

    @patch("src.whisper_converter.whisper.load_model")
    @patch("os.path.exists")
    def test_convert_to_text_success(self, mock_exists, mock_load_model):
        """Test successful text conversion."""
        mock_exists.return_value = True
        mock_model = Mock()
        mock_model.transcribe.return_value = {"text": "  Hello world  "}
        mock_load_model.return_value = mock_model

        converter = WhisperConverter()
        result = converter.convert_to_text("test.m4a")

        assert result == "Hello world"
        mock_model.transcribe.assert_called_once_with("test.m4a", language=None)

    @patch("src.whisper_converter.whisper.load_model")
    @patch("os.path.exists")
    def test_convert_to_text_with_language(self, mock_exists, mock_load_model):
        """Test text conversion with specified language."""
        mock_exists.return_value = True
        mock_model = Mock()
        mock_model.transcribe.return_value = {"text": "こんにちは"}
        mock_load_model.return_value = mock_model

        converter = WhisperConverter()
        result = converter.convert_to_text("test.m4a", language="ja")

        assert result == "こんにちは"
        mock_model.transcribe.assert_called_once_with("test.m4a", language="ja")

    @patch("src.whisper_converter.whisper.load_model")
    @patch("os.path.exists")
    def test_convert_to_text_file_not_found(self, mock_exists, mock_load_model):
        """Test conversion with non-existent file."""
        mock_exists.return_value = False
        mock_load_model.return_value = Mock()

        converter = WhisperConverter()

        with pytest.raises(
            FileNotFoundError, match="Audio file not found: nonexistent.m4a"
        ):
            converter.convert_to_text("nonexistent.m4a")

    @patch("src.whisper_converter.whisper.load_model")
    @patch("os.path.exists")
    def test_convert_to_text_transcribe_failure(self, mock_exists, mock_load_model):
        """Test transcription failure."""
        mock_exists.return_value = True
        mock_model = Mock()
        mock_model.transcribe.side_effect = Exception("Transcription failed")
        mock_load_model.return_value = mock_model

        converter = WhisperConverter()

        with pytest.raises(
            Exception, match="Failed to transcribe audio: Transcription failed"
        ):
            converter.convert_to_text("test.m4a")

    @patch("src.whisper_converter.whisper.load_model")
    def test_convert_to_text_no_model(self, mock_load_model):
        """Test conversion when model is not loaded."""
        mock_load_model.return_value = None

        converter = WhisperConverter()
        converter.model = None  # Simulate model loading failure

        with pytest.raises(Exception, match="Whisper model not loaded"):
            converter.convert_to_text("test.m4a")
