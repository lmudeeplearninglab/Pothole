import cv2 
import numpy as np
import os
import pickle 

# runs locally 
import image_CropResize as icr 

#img = cv2.imread('0a0ba96d-7859aaa6.jpg')
#cv2.imshow('0a0ba96d-7859aaa6.jpg', img)
#k = cv2.waitKey(0)
print('* Successfully ran the showing...')
#testing(img)

def preprocessing(img): 
    #from image_CropResize file:
    # 120 and 320 are random input values; must be replaced with the exact 
    #  coordinates using Conor's extract_road function 
    image = icr.cropResizeImage(image, 120,320)
    # Crop and Resize snippet from Conor's code 
    # for testing purposes only: 
    # print(type(img))
    return img 

def serialize_images(dir): 
    # sets first directory: training images (but can be changed in the real program)
    directory = dir + "/training/" 
    # print("* Directory TYPE is ")
    # print( type(directory))
    # print("* Directory is ")
    # print( directory)
    direct_images = os.listdir(directory)
    # print("* Direct_images TYPE is ")
    # print(type(direct_images))
    
    # setting up the lists to create dictionary
    images = [] 
    labels = [] 
    count = 0
    
    for image in direct_images: 
        # read the image using directory 
        image = cv2.imread(directory + image)
        # preprocess image 
        image = preprocessing(image)
        # for testing purposes: 
        # print(type(image))
        
        # add to corresponding list 
        images.append(image) 
        labels.append(1)
    return (images, labels) 

