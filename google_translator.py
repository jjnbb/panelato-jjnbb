from googletrans import Translator

class GoogleTranslator:
    def __init__(self):
        self.translator = Translator()

    def translate_text(self, text):
        translation = self.translator.translate(text, dest='en')
        return translation.text