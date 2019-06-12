#Connected Components

import cv2
src = cv2.imread('/directorypath/image.bmp')
ret, thresh = cv2.threshold(src,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
connectivity = 4
output = cv2.connectedComponentsWithStats(thresh, connectivitiy, cv2.CV_32S)
num_labels = output [0]
labels = output[1]
stats = output [2]
centroids = output [3]


#Source:https://stackoverflow.com/questions/35854197/how-to-use-opencvs-connected-components-with-stats-in-python

