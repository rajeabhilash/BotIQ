import cv2
import numpy as np

# Read the image
img = cv2.imread("Image_3.png")

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply adaptive thresholding
thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

# Find the contours in the image
contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Iterate through the contours and find the one with the largest area
max_area = 0
max_contour = None
for contour in contours:
    area = cv2.contourArea(contour)
    if area > max_area:
        max_area = area
        max_contour = contour

# Draw the table contour on the original image
cv2.drawContours(img, [max_contour], 0, (0, 255, 0), 2)

# Create a mask of the table region
mask = np.zeros(img.shape, dtype=np.uint8)
cv2.drawContours(mask, [max_contour], 0, (255, 255, 255), -1)

# Apply the mask to the original image to color the table
table = np.bitwise_and(img, img, mask)

# Show the image
cv2.imshow("Table", table)
cv2.waitKey(0)
cv2.destroyAllWindows()
