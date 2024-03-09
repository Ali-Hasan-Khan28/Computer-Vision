import cv2
import numpy as np

def non_maximum_suppression(image, gradient_magnitude, gradient_direction):
    rows, cols = image.shape
    suppressed_image = np.copy(image)

    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            center_value = gradient_magnitude[i, j]

            if gradient_direction[i, j] == 0:
                neighbors = [gradient_magnitude[i, j-1], gradient_magnitude[i, j+1]]
            elif gradient_direction[i, j] == 45:
                neighbors = [gradient_magnitude[i-1, j+1], gradient_magnitude[i+1, j-1]]
            elif gradient_direction[i, j] == 90:
                neighbors = [gradient_magnitude[i-1, j], gradient_magnitude[i+1, j]]
            elif gradient_direction[i, j] == 135:
                neighbors = [gradient_magnitude[i-1, j-1], gradient_magnitude[i+1, j+1]]

            if center_value <= max(neighbors):
                suppressed_image[i, j] = 0

    return suppressed_image



def calculate_gradient_magnitude(gray_image):
    # Calculate gradients using Sobel operators
    gradient_x = cv2.Sobel(gray_image, cv2.CV_64F, 1, 0, ksize=3)
    gradient_y = cv2.Sobel(gray_image, cv2.CV_64F, 0, 1, ksize=3)

    # Calculate the magnitude of the gradient
    gradient_magnitude = np.sqrt(gradient_x**2 + gradient_y**2)

    return gradient_magnitude

def calculate_gradient_direction(gray_image):
    # Calculate gradients using Sobel operators
    gradient_x = cv2.Sobel(gray_image, cv2.CV_64F, 1, 0, ksize=3)
    gradient_y = cv2.Sobel(gray_image, cv2.CV_64F, 0, 1, ksize=3)

    # Calculate the arctangent of the gradient
    gradient_direction = np.arctan2(gradient_y, gradient_x) * (180 / np.pi)

    return gradient_direction

def quantize_gradient_direction(gradient_direction):
    # Quantize gradient direction into 0, 45, 90, 135 degrees
    quantized_direction = np.zeros_like(gradient_direction, dtype=np.uint8)

    quantized_direction[(gradient_direction >= -22.5) & (gradient_direction < 22.5)] = 0
    quantized_direction[(gradient_direction >= 22.5) & (gradient_direction < 67.5)] = 45
    quantized_direction[(gradient_direction >= 67.5) & (gradient_direction < 112.5)] = 90
    quantized_direction[(gradient_direction >= 112.5) | (gradient_direction < -112.5)] = 135

    return quantized_direction

def non_maximum_suppression(image, gradient_magnitude, gradient_direction):
    rows, cols = image.shape
    suppressed_image = np.copy(image)

    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            center_value = gradient_magnitude[i, j]

            if gradient_direction[i, j] == 0:
                neighbors = [gradient_magnitude[i, j-1], gradient_magnitude[i, j+1]]
            elif gradient_direction[i, j] == 45:
                neighbors = [gradient_magnitude[i-1, j+1], gradient_magnitude[i+1, j-1]]
            elif gradient_direction[i, j] == 90:
                neighbors = [gradient_magnitude[i-1, j], gradient_magnitude[i+1, j]]
            elif gradient_direction[i, j] == 135:
                neighbors = [gradient_magnitude[i-1, j-1], gradient_magnitude[i+1, j+1]]

            if center_value <= max(neighbors):
                suppressed_image[i, j] = 0

    return suppressed_image
# Example usage
image = cv2.imread("C:/Users/hp/OneDrive/Desktop/5thS/6th Semester Courses/Computer Vision/CV Assignment 1/Computer-Vision/Assigment01/ec/data/img03.jpg", cv2.IMREAD_GRAYSCALE)
# Perform edge detection, gradient calculation, and quantize gradient direction (0, 45, 90, 135)
# (Code for these steps is not included here)
gradient_magnitude = calculate_gradient_magnitude(image)
gradient_direction = quantize_gradient_direction(calculate_gradient_direction(image))

# Apply Non-Maximum Suppression
result = non_maximum_suppression(image, gradient_magnitude, gradient_direction)

# Display the result
cv2.imshow("Original Image", image)
cv2.imshow("NMS Result", result)
cv2.waitKey(0)
cv2.destroyAllWindows()
