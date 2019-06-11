# create a folder to store extracted images
import os
folder = 'test'  
os.mkdir(folder)
# use opencv to convert avi video into images 
import cv2
print(cv2.__version__)  
vidcap = cv2.VideoCapture('video file name')
count = 0
while True:
    success,image = vidcap.read()
    if not success:
        break
    cv2.imwrite(os.path.join(folder,"frame{:d}.jpg".format(count)), image)     # save frame as JPEG file
    count += 1
print("{} images are extracted in {}.".format(count,folder))
