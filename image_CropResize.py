
#Crop and Resize a image 
#inputs:   image - a numpy array of the original image
#           bbsize - a list of bounding box and new size information
#           (bbsize[0], bbsize[1]) - starting point of the bounding box (x1, y1)
#           (bbsize[2], bbsize[3]) - ending point of the bounding box (x2, y2) 
#           bbsize[4]  - the width of the output image
#           bbsize[5] - the height of the output image
 
import numpy as np
import cv2
def cropResizeImage(image, bbsize):
    #x1 = bbsize[0]
    #y1 = bbsize[1]
    #x2 = bbsize[2]
    #y2 = bbsize[3]
    #w = list[4]
    #h = list[5]
    crop = image[bbsize[0]:bbsize[1], bbsize[2]:bbsize[3]]
    # For testing purposes:
    #print("* Printing crop")
    #print(crop)
  
    #Resizing
    #INTER_CUBIC - a bicubic interpolation over 4x4 pixel neighborhood
  
    dim = (bbsize[4],bbsize[5])
    # For testing purposes: 
    #print(dim)
    new_image = cv2.resize(crop, dim, interpolation =cv2.INTER_CUBIC)
    return new_image
