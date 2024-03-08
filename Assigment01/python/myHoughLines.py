# import numpy as np
# import cv2  # For cv2.dilate function

# def myHoughLines(H, nLines):
#     # YOUR CODE HERE


import numpy as np
from scipy.ndimage import maximum_filter

def myHoughLines(img_hough, nLines):
    # Apply non-maximal suppression to the Hough accumulator
    local_maxima = maximum_filter(img_hough, size=(5, 5), mode='constant')
    hough_peaks = np.where((img_hough == local_maxima) & (img_hough > 0))

    # Sort the peaks based on their accumulator values in descending order
    sorted_indices = np.argsort(-img_hough[hough_peaks])
    sorted_peaks = (hough_peaks[0][sorted_indices], hough_peaks[1][sorted_indices])

    # Select the top nLines peaks
    selected_peaks = (sorted_peaks[0][:nLines], sorted_peaks[1][:nLines])

    # Convert peak coordinates to ρ and θ values
    rhos = selected_peaks[0] - (img_hough.shape[0] // 2)
    thetas = np.deg2rad(selected_peaks[1])

    return rhos, thetas