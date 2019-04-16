'''
Author: Conor Green
Description: Provides functionality for renaming; filtering by hue,
saturation, and value; and cropping
Usage: Call functions through other script
Version:
1.0 - April 7 2019 - Basic functionality to learn libraries
1.1 - April 8 2019 - Added better code structure
1.2 - April 8 2019 - Works as intended. Still requires paramter tuning
1.3 - April 8 2019 - Added daylight or not classification
1.4 - April 8 2019 - Added slideshow functionality
1.5 - April 8 2019 - Fixed bugs, tuned daylight, better coding style
1.6 - April 15 2019 - Fixed how the program renames files
'''
##colorizer.org

import cv2
import matplotlib.pyplot as plt
import numpy as np
import os
import time

def rename_all_(path):
    i = highest_num_image(new_path) + 1

    for filename in os.listdir(path):
        old_file = os.path.join(path,filename)
        new_file = os.path.join(path, "image" + str(i) + ".jpg")
        os.rename(old_file , new_file)
    return

def rename_this_many_(path , new_path , count):
    start_pt = highest_num_image(new_path) + 1

    for i in range(start_pt, start_pt + count):
        filename = os.listdir(path)[i]
        old_file = os.path.join(path,filename)
        new_file = os.path.join(new_path, "image" + str(i) + ".jpg")
        os.rename(old_file , new_file)
    return

def highest_num_image(path):
    highest = 0
    for filename in os.listdir(path):
        radix = filename.find(".")
        temp = filename[5:radix]
        if int(temp) > highest:
            highest = int(temp)

    return highest

def get_avg_val(hsv_image):
    sum = 0
    h , w , d = hsv_image.shape

    for i in range(0,h):
        for j in range(0,w):
            sum += hsv_image[i,j,2]

    avg_value = sum/(w*h)

    return avg_value

def is_daytime(hsv_image):
    #paramter
    threshold = 120 #/255

    is_day = True

    avg_val = get_avg_val(hsv_image)

    if avg_val < threshold:
        is_day = False

    return is_day

def classify_hsv_image(hsv_image, verbose):
    classification = "not daylight"

    if is_daytime(hsv_image) == True:
        classification = "daylight"


    if verbose == True:
        print classification

    return classification

def get_mask(im_class , im_hsv ):
    if im_class == "daylight":
        return cv2.inRange(im_hsv,(0,0,80),(255,60,150))

    #default
    #elif im_class == "not daylight":
    return cv2.inRange(im_hsv,(0,0,100),(255,150,230))

def clean_noise(image, (kernel_h , kernel_w) ):
    kernel = np.ones(( kernel_h , kernel_w ));

    image = cv2.erode(image, kernel , iterations=1)

    image = cv2.dilate(image, kernel , iterations =1)

    return image

'''
    Set h = 640 and w = 380
'''
def resize(image , desired_h , desired_w ):
    im_h , im_w , im_d = image.shape

    image = cv2.resize(image, () , interpolation = cv2.INTER_AREA)

    return

def crop(image,  w_factor , h_factor):
    im_h , im_w , im_d = image.shape
    new_w = int(im_w*w_factor)
    new_h = int(im_h*h_factor)
    h1 =int( (im_h/2) - new_h )
    h2 =int( (im_h/2)+ new_h )


    crop_im = image[h1:h2 -500 , 0:new_w , :]

    return ( image , crop_im )


def process_image(image_path , verbose):
    im = cv2.imread(image_path)

    orig_image = cv2.cvtColor(im,cv2.COLOR_BGR2RGB)

    #hue saturation value
    im_hsv = cv2.cvtColor(orig_image,cv2.COLOR_BGR2HSV)

    im_class = classify_hsv_image(im_hsv , verbose)

    mask = get_mask(im_class , im_hsv )

    im = cv2.bitwise_and(orig_image,orig_image,mask = mask)

    kernel_dim = ( 20 , 20 )

    filter = clean_noise(im , kernel_dim)

    filter[filter>0] = 1

    proc_image = orig_image*filter

    return (orig_image , proc_image)

def slideshow_images(path , number , pause_length , verbose):
    for i in range(0,number):
        file_number = i

        image_path = os.path.join(path, "image" + str(file_number) + ".jpg")


        (orig_image, proc_image) = process_image(image_path , verbose = verbose)

        (orig_image , cropped_image ) = crop(proc_image, 1 , .5)

        plt.figure()

        plt.subplot(2,1,1)
        plt.imshow(orig_image)

        plt.subplot(2,1,2)
        plt.imshow(cropped_image)

        plt.show(block=False)

        time.sleep(pause_length)

        plt.close()

    return

def rename_crop_slideshow():
    additional_path ="bdd100k/images/10k/test"
    current_directory = ""
    data_path = additional_path + current_directory

    new_path = "renamed_images"
    #"~/Documents/University/Junior Year/Second Semester/Pothole Detection/bdd100k/images/10k/test"

    count = 20
    verbose = True


    rename_this_many_(data_path , new_path , count)

    slideshow_images(new_path , count , 10 , verbose)

    '''
    Crop image into small rectangle
    cv2.resize()

    see also: cv2.GaussianBlur()
    '''
    return

def main():
    rename_crop_slideshow()
    return

if __name__ == "__main__":
    main()
