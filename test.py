from PIL import Image
import pytesseract

print(pytesseract.image_to_string(Image.open('images/m20-217-risen-reef.jpg')))
