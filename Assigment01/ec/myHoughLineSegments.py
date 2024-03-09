import numpy as np

def myHoughLineSegments(lineRho, lineTheta, Im):
    lines = []

    for i in range(len(lineRho)):
        rho = lineRho[i]
        theta = lineTheta[i]

        # Calculate the start and end points of the line segment
        x1 = int(rho * np.cos(theta))
        y1 = int(rho * np.sin(theta))
        x2 = int(x1 - 1000 * np.sin(theta))
        y2 = int(y1 + 1000 * np.cos(theta))

        # Ensure the points are within the image bounds
        x1, y1, x2, y2 = clip_line_segment(x1, y1, x2, y2, Im.shape[1], Im.shape[0])

        lines.append(((x1, y1), (x2, y2)))

    return lines

def clip_line_segment(x1, y1, x2, y2, width, height):
    # Clip the line segment to ensure it stays within the image bounds
    x1 = max(0, min(x1, width - 1))
    y1 = max(0, min(y1, height - 1))
    x2 = max(0, min(x2, width - 1))
    y2 = max(0, min(y2, height - 1))

    return x1, y1, x2, y2
