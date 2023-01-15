import pdf2image
import pytesseract
import cv2
import pandas as pd


TESSERACT_PATH = r'C:\Users\abhilash_chavhan\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'
POPPELER_BIN_PATH = r'C:\poppler\Library\bin'


def pdf_to_img(pdf_file):
    return pdf2image.convert_from_path(pdf_file, poppler_path=POPPELER_BIN_PATH)


def ocr_core(file):
    text = pytesseract.image_to_string(file)
    return text


def print_pages(pdf_file):
    images = pdf_to_img(pdf_file)
    images[3].save('Image_3.png','PNG')
    img = cv2.imread('Image_3.png')
    # Apply Otsu threshold
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # Find contours in the thresholded image
    contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Find the contour with the largest area (this should be the table)
    largest_contour = max(contours, key=cv2.contourArea)

    # Get the bounding rectangle of the table
    x, y, w, h = cv2.boundingRect(largest_contour)

    # Crop the table out of the image
    table = img[y:y + h, x:x + w]

    # Convert the table to grayscale
    gray_table = cv2.cvtColor(table, cv2.COLOR_BGR2GRAY)

    # Set the tesseract OCR configuration
    config = ("-l eng --oem 1 --psm 3")

    # Get the text from the image
    text = pytesseract.image_to_string(gray_table, config=config)

    # Split the text into lines
    lines = text.split("\n")

    # Split each line into words
    columns = []
    for line in lines:
        words = line.split()
        columns.append(words)

    # Create a DataFrame from the columns
    df = pd.DataFrame(columns)

    # Export the DataFrame to an Excel file
    df.to_excel("table.xlsx", index=False)

    # for pg, img in enumerate(images):
    #     print(ocr_core(img))


print_pages(r"D:\Zoetis\UserData\ROW factors - January 2023.pdf")