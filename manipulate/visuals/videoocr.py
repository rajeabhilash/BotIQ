import requests
import pytesseract
from PIL import Image
from PIL import ImageFilter
from io import BytesIO

import cv2


def ocr_in_video():
    video = cv2.VideoCapture(0)
    while True:
        ret, frame = video.read()

        h, w, c = frame.shape
        boxes = pytesseract.image_to_boxes(frame)
        for b in boxes.splitlines():
            b = b.split(' ')
            frame = cv2.rectangle(frame, (int(b[1]), h - int(b[2])), (int(b[3]), h - int(b[4])), (0, 255, 0), 2)

        cv2.imshow('Showing Frame to text of Image', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    video.release()
    cv2.destroyAllWindows()
