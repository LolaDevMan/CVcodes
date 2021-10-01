import cv2
import numpy as np

# Load image
im = cv2.imread('red.jpeg')

# Define the blue colour we want to find - remember OpenCV uses BGR ordering
blue = [42,0,213]

# Get X and Y coordinates of all blue pixels
X,Y = np.where(np.all(im==blue,axis=2))

print(X,Y)