import pytesseract
from PIL import Image, ImageEnhance, ImageFilter
import Pics



pytesseract.pytesseract.tesseract_cmd = 'C:\\Python36-32\\Lib\\Tesseract-OCR\\tesseract.exe'
im = Image.open(Pics.Test.pic4) # the second one
im = im.filter(ImageFilter.MedianFilter())
enhancer = ImageEnhance.Contrast(im)
im = enhancer.enhance(2)
im = im.convert('1')
im.save('text.png')
text = pytesseract.image_to_string(Image.open('text.png'))

print(text)

try:
    import Image
except ImportError:
    from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:\\Python36-32\\Lib\\Tesseract-OCR\\tesseract.exe'
# Include the above line, if you don't have tesseract executable in your PATH
# Example tesseract_cmd: 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract'

print(pytesseract.image_to_string(Image.open(Pics.Test.pic4)))
#print(pytesseract.image_to_string(Image.open('test-european.jpg'), lang='fra'))