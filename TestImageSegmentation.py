import cv2 
import numpy as np 
import image_segmentation as isp
import matplotlib.pyplot as plt


one, two, three = isp.segment_im_file('pexels-photo-490466.jpeg')
print("test")
print(one)
print(two)
print(three)
plt.figure()
plt.imshow(one)
plt.show()
