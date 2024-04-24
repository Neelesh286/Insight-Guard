import cv2
import numpy as np

# Read the image
image = cv2.imread('coin.jpeg')

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Gaussian blur to reduce noise
blurred = cv2.GaussianBlur(gray, (5, 5), 0)

# Detect edges using Canny edge detector
edges = cv2.Canny(blurred, 30, 150)

# Find contours in the edge-detected image
contours, _ = cv2.findContours(edges.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Filter contours based on area and approximation of circularity
for contour in contours:
    # Calculate the area of the contour
    area = cv2.contourArea(contour)
    
    # Approximate the contour to a polygon
    perimeter = cv2.arcLength(contour, True)
    approx = cv2.approxPolyDP(contour, 0.04 * perimeter, True)
    
    # If the contour is approximately circular
    if len(approx) > 8 and area > 1000:
        # Fit an ellipse around the contour
        ellipse = cv2.fitEllipse(contour)
        
        # Draw the ellipse on the original image
        cv2.ellipse(image, ellipse, (0, 255, 0), 2)

# Display the result
cv2.imshow('Ellipse Detection', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
