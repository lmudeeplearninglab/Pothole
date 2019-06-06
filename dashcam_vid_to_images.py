# Importing all necessary libraries 
import cv2 
import os 
  
def convert_avi_to_mp4(avi_file_path, output_name):
    os.popen("command[, mode[, bufsize]]".format(input = avi_file_path, output = output_name))
    return True 

# Read the video from specified path 
cam = cv2.VideoCapture("output_name.mp4") 
  
try: 
      
    # creating a folder named data 
    if not os.path.exists('data'): 
        os.makedirs('data') 
  
# if not created then raise error 
except OSError: 
    print ('Error: Creating directory of data') 
  
# frame 
currentframe = 0

while(True): 
      
    # reading from frame 
    ret,frame = cam.read() 
  
    if ret: 
        # if video is still left continue creating images 
        name = './data/frame' + str(currentframe) + '.jpg'
        print ('Creating...' + name) 
  
        # writing the extracted images 
        cv2.imwrite(name, frame) 
  
        # increasing counter so that it will 
        # show how many frames are created 
        currentframe += 1
    else: 
         break
