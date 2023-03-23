import cv2
import numpy as np

# Load the image
img = cv2.imread('a.png')

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply Gaussian blur to the image
blur = cv2.GaussianBlur(gray, (5, 5), 0)

# Apply Canny edge detection to the image
edges = cv2.Canny(blur, 100, 200)

# Apply thresholding to the image
ret, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

# Combine all the effects
combined = np.hstack((gray, blur, edges, thresh))

# Show the original and combined images
cv2.imshow('Original', img)
cv2.imshow('Combined', combined)

# Wait for a key press and then close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()