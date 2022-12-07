try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
import streamlit as st
from PIL import Image


config = ('-l urd --oem 1 --psm 7')

def ocr_core(filename):
    """
    This function will handle the core OCR processing of images.
    """
    # We'll use Pillow's Image class to open the image and pytesseract to detect the string in the image
    
    text = pytesseract.image_to_string(Image.open(filename),config=config)
    return text


def app():
    image_file=st.file_uploader(label='Upload Image File', type=['png','jpg','jpeg'])
    if image_file is not None:
        image=Image.open(image_file).convert('L') 
        st.image(image)
        text=ocr_core(image_file)
        st.write(text)

app()
