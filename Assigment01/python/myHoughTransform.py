import numpy as np

def myHoughTransform(img_threshold, rhoRes, thetaRes):
    # Define the maximum possible ρ value (M)
    max_rho = int(np.sqrt(img_threshold.shape[0]**2 + img_threshold.shape[1]**2))

    # Define ρ and θ scales
    rhoScale = np.arange(0, max_rho + 1, rhoRes)
    thetaScale = np.deg2rad(np.arange(0, 180, thetaRes))

    # Initialize Hough transform accumulator
    img_hough = np.zeros((len(rhoScale), len(thetaScale)), dtype=int)
    print(img_hough.shape)

    # Iterate over edge points in the thresholded image
    edge_points = np.argwhere(img_threshold > 0)
    i = 0
    for point in edge_points:
        y, x = point
        if i%100 == 0:
            print(i, "done")
        # Iterate over possible θ values
        for j, theta in enumerate(thetaScale):
            rho = int(x * np.cos(theta) + y * np.sin(theta))
            rho_index = np.abs(rhoScale - rho).argmin()

            # Increment the accumulator cell
            img_hough[rho_index, j] += 1
        i = i+1
        if i == 21245:
            break

    return img_hough, rhoScale, thetaScale
