
#import library
import numpy as np
import cv2
import os
from pathlib import Path
import re
import time

#enter the file name 

print("Enter the File Name:")
file_name = input()
#start recording 
cap = cv2.VideoCapture(0)
#defining the protocol 
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('test.avi', fourcc, 60, (320, 240))

#fourcc = cv2.VideoWriter_fourcc(*'MP4V')
#out = cv2.VideoWriter(str(file_name)+'.mp4', fourcc, 20.0, (640, 480)) 

#video will record till Q or ESC pressed
while 1:
    ret, img = cap.read()
    out.write(img)
    
    cv2.imshow('img',img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
