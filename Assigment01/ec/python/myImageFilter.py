# import numpy as np

# def myImageFilter(img0, h):
#     print("sdfdf")
import numpy as np
import cv2
def myImageFilter(img0, h):
    # Get the dimensions of the image and filter
    img_height, img_width = img0.shape
    filter_height, filter_width = h.shape

    # Calculate padding for the convolution
    pad_height = filter_height // 2
    pad_width = filter_width // 2

    # Pad the image with zeros
    img_padded = np.pad(img0, ((pad_height, pad_height), (pad_width, pad_width)), mode='constant')

    # Initialize the output image
    img1 = np.zeros_like(img0, dtype=float)

    # Perform convolution
    for i in range(img_height):
        for j in range(img_width):
            img1[i, j] = np.sum(img_padded[i:i + filter_height, j:j + filter_width] * h)

    return img1

