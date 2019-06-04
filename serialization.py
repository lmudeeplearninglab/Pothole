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
    #from ericson and casey's file: 
    # set image to result of the file 
    print(type(img))
    # set random values to form a square bound 
    bbsize = [400, 400, 620, 620, 200, 200]
    img = icr.cropResizeImage(img, bbsize)
    print(type(img))
    return img 

def serialize_images(dir): 
    # sets first directory: training images (but can be changed in the real program)
    directory = dir + "/training/" 
    print("* Directory TYPE is ")
    print( type(directory))
    print("* Directory is ")
    print( directory)
    direct_images = os.listdir(directory)
    print("* Direct_images TYPE is ")
    print(type(direct_images))
    print("* Direct_images is ")
    print( direct_images)
    
    # setting up the lists to create dictionary
    print("* Setting up lists...")
    images = [] 
    labels = [] 
    print("* Starting for loop...")
    count = 0
    
    for image in direct_images: 
        # read the image using directory 
        print("* In For loop")
        count = count + 1 
        print("* Count is ")
        print(count)
        image = cv2.imread(direct_images[count])
        #image = cv2.imread(direct_images + image)
        # preprocess image 
        image = preprocessing(image)
        # add to corresponding list 
        images.append(image) 
        labels.append(1)
    
    print("* Out of For loop")
    print(type(images))
    print(type(labels))

