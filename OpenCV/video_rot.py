
# coding: utf-8

# In[24]:


import cv2
import time


# In[85]:


cap=cv2.VideoCapture(0)  #opening camera


# In[86]:


cap.set(3, 800) #width
cap.set(4, 600) #height
angle =0
ang=0
while cap.isOpened():
    if angle == 360 or ang==360:
        angle =0
        ang=0
    angle = angle + 10
    ang=ang-10
    
    ret, framee = cap.read()    #reading the frame
    
    frame = cv2.cvtColor(framee, cv2.COLOR_BGR2GRAY)  #converting to gray scale
    frame=cv2.flip(frame,90)
    
    row, col = frame.shape
    
    # Defining the point for rotation, angle and scaling
    
    R = cv2.getRotationMatrix2D((col/2, row/2), angle, 0.5)  # Translation matrix
    frame=cv2.warpAffine(frame, R, (col, row))

    cv2.imshow('video',frame)
    
    fram = cv2.cvtColor(framee, cv2.COLOR_BGR2GRAY)
    fram=cv2.flip(fram,90)
    row, col = fram.shape
    R1 = cv2.getRotationMatrix2D((col/2, row/2), ang, 0.5)
    fram=cv2.warpAffine(fram, R1, (col, row))

    cv2.imshow('video1',fram)

    
    if cv2.waitKey(1)==27:
        break


# In[87]:


cv2.destroyAllWindows()    
cap.release()

