import cv2
import numpy as np
import pytesseract

class ImageProcessor:
    def __init__(self, image):
        self.image = cv2.imdecode(np.frombuffer(image.read(), np.uint8), 1)
        self.original_text = ""

    def extract_text(self):
        gray_image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        text = pytesseract.image_to_string(gray_image)
        return text
