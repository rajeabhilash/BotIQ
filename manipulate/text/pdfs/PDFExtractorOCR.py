import pdf2image
import pytesseract
from PIL import Image

def pdf_to_img(pdf_file):
    return pdf2image.convert_from_path(pdf_file)


def ocr_core(file):
    text = pytesseract.image_to_string(file)
    return text


def print_pages(pdf_file):
    images = pdf_to_img(pdf_file)
    for pg, img in enumerate(images):
        print(ocr_core(img))


print_pages(r"D:\Zoetis\UserData\ROW factors - January 2023.pdf")