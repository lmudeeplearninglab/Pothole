
#Crop and Resize a image 
 
import numpy as np
import cv2

def cropResizeImage(image, desired_h, desired_w):
 # taken from image_manipulation.py by Conor Green, LMU EE
 
 # print("* Original image shape is: ")
 # print(image.shape)
 
 # resize using cv2 function 
 # cv2.INTER_AREA is used to shrink image 
 image = cv2.resize(image, (140,220), interpolation =cv2.INTER_AREA)
 
 # defining lengths and heights in preparation for cropping 
 xl = 120
 xh = 360
 yl = 120
 yh = 360
 crop_im = image[xl:xh, yl:yh, :]
 
 # For clarification on the typings: 
 # print("* Cropped image's type is: ")
 # print(type(crop_im))
 # print("* Cropped image shape is: ")
 # print(crop_im.shape)
 return (crop_im)
