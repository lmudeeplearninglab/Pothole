#Connected Components

import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('downloads/grad2.jpg',0)
ret,thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
plt.imshow(thresh1, cmap = 'gray', interpolation = 'bicubic')

plt.show()

connectivity = 4
output = cv2.connectedComponentsWithStats(thresh1, connectivity, cv2.CV_32S)
num_labels = output [0]
labels = output[1]
stats = output [2]
centroids = output [3]
print(num_labels)

#Source:https://stackoverflow.com/questions/35854197/how-to-use-opencvs-connected-components-with-stats-in-python

