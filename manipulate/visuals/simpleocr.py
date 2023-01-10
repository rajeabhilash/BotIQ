import requests
import pytesseract
from PIL import Image
from PIL import ImageFilter
from io import BytesIO
import cv2


def get_url_image(url):
    return Image.open(BytesIO(requests.get(url, verify=False).content))


def get_local_image(image_path):
    return Image.open(image_path, 'r')


def get_text_from_image(data, islocal):
    image = get_url_image(data) if not islocal else get_local_image(data)
    image.filter(ImageFilter.SHARPEN)
    return pytesseract.image_to_string(image)


def get_dict_from_image(data):
    image = cv2.imread(data)
    return pytesseract.image_to_data(image, output_type=pytesseract.Output.DICT)


def get_brackets_to_text(data):
    # image = get_url_image(data) if not islocal else get_local_image(data)
    # image.filter(ImageFilter.SHARPEN)
    image = cv2.imread(data)
    h, w, c = image.shape
    boxes = pytesseract.image_to_boxes(image)
    for b in boxes.splitlines():
        b = b.split(' ')
        image = cv2.rectangle(image, (int(b[1]), h - int(b[2])), (int(b[3]), h - int(b[4])), (0, 255, 0), 2)
    cv2.imshow('Rectangle Around Text', image)
    cv2.waitKey(0)
