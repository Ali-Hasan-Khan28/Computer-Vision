# import numpy as np
# from scipy import signal    # For signal.gaussian function

# from myImageFilter import myImageFilter

# def myEdgeFilter(img0, sigma):
#     # YOUR CODE HERE
#     print("Sdsdsdsds")


import numpy as np
from scipy import signal
import cv2
from myImageFilter import myImageFilter
def myEdgeFilter(img0, sigma):
    # Gaussian smoothing
    filter_size = int(2 * np.ceil(3 * sigma) + 1)
    gaussian_filter = signal.gaussian(filter_size, std=sigma).reshape(-1, 1)
    gaussian_kernel = np.outer(gaussian_filter, gaussian_filter)

    img_smoothed = signal.convolve2d(img0, gaussian_kernel, mode='same', boundary='symm')

    # Sobel filters
    sobel_x = np.array([[-1, 0, 1]])
    sobel_y = np.array([[-1], [0], [1]])

    # Convolve with Sobel filters to find gradients
    img_x = signal.convolve2d(img_smoothed, sobel_x, mode='same', boundary='symm')
    img_y = signal.convolve2d(img_smoothed, sobel_y, mode='same', boundary='symm')

    # Compute gradient magnitude and orientation
    gradient_magnitude = np.sqrt(img_x**2 + img_y**2)
    gradient_orientation = np.arctan2(img_y, img_x) * (180 / np.pi)

    # Map the gradient angles to the closest of 4 cases
    gradient_orientation = np.abs(gradient_orientation)
    gradient_orientation[np.where(gradient_orientation > 67.5)] = 90.0
    gradient_orientation[np.where((gradient_orientation >= 22.5) & (gradient_orientation <= 67.5))] = 45.0
    gradient_orientation[np.where((gradient_orientation >= 0) & (gradient_orientation < 22.5))] = 0.0
    gradient_orientation[np.where((gradient_orientation >= 112.5) & (gradient_orientation < 157.5))] = 135.0

    # Non-maximum suppression
    img1 = np.zeros_like(img0, dtype=float)

    for i in range(1, img0.shape[0] - 1):
        for j in range(1, img0.shape[1] - 1):
            angle = gradient_orientation[i, j]

            # Check the neighboring pixels along the gradient direction
            if angle == 0.0:
                neighbors = [gradient_magnitude[i, j - 1], gradient_magnitude[i, j + 1]]
            elif angle == 45.0:
                neighbors = [gradient_magnitude[i - 1, j - 1], gradient_magnitude[i + 1, j + 1]]
            elif angle == 90.0:
                neighbors = [gradient_magnitude[i - 1, j], gradient_magnitude[i + 1, j]]
            elif angle == 135.0:
                neighbors = [gradient_magnitude[i - 1, j + 1], gradient_magnitude[i + 1, j - 1]]

            # Perform non-maximum suppression
            if gradient_magnitude[i, j] >= max(neighbors):
                img1[i, j] = gradient_magnitude[i, j]

    return img1