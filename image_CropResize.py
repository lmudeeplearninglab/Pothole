
#Crop and Resize a image 
 
import numpy as np
import cv2
def cropResizeImage(image, bbsize):
       # taken from image_manipulation.py by Conor Green, LMU EE

    # print("* Original image shape is: ")
    # print(image.shape)
    # resize using cv2 function 
    # cv2.INTER_AREA is used to shrink image 
    image = cv2.resize(image, (140,220), interpolation =cv2.INTER_AREA)
    # print("* New image shape is: ")
    # print(image.shape)
    
    # defining length and heights in preparation for cropping 
    xl = 360
    xh = 600
    yl = 540
    yh = 400
    new_image = image[xl:xh, yl:yh, :]
    
    # For clarification on the typings: 
    # print("* Cropped image's type is: ")
    # print(type(new_image))
    # print("* Cropped image shape is: ")
    # print(crop_im.shape)
    return new_image
