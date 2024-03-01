from image_processor import ImageProcessor
from google_translator import GoogleTranslator

class MangaTranslator(ImageProcessor, GoogleTranslator):
    def __init__(self, image):
        super().__init__(image)

    def translate(self):
        self.original_text = self.extract_text()
        translated_text = self.translate_text(self.original_text)
        return translated_text
