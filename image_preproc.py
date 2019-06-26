#Crop and Resize a image 
 
import numpy as np
import cv2 
import image_segmentation as isp
 # defining lengths and heights in preparation for cropping 
(width, height) = 0,0 
 
def extractRoad(image):
    thresh = 30
    idx = np.logical_and(abs(image[:,:,0]-image[:,:,1])<=thresh, abs(image[:,:,1]-image[:,:,2])<=thresh);
    return idx

 
def cropResizeImage(image, bounds, desired_h, desired_w):
    width = desired_w
    height = desired_h
    # taken from image_manipulation.py by Conor Green, LMU EE
 
    # print("* Original image shape is: ")
    # print(image.shape)
    xl = bounds[0]
    xh = bounds[2]
    yl = bounds[1]
    yh = bounds[3]
    crop_im = image[yl:yh, xl:xh, :]
    # resize using cv2 function 
    # cv2.INTER_AREA is used to shrink image 
    img = cv2.resize(image, (desired_h,desired_w), interpolation =cv2.INTER_AREA)
    # For clarification on the typings: 
    # print("* Cropped image's type is: ")
    # print(type(crop_im))
    # print("* Cropped image shape is: ")
    # print(crop_im.shape)
    return (img)

