
# coding: utf-8

# In[1]:


import cv2
import numpy as np


# In[2]:


cap=cv2.VideoCapture(0) # opening default camera


while cap.isOpened():

    
    ret, framee = cap.read()    #reading the frame
    
    frame = cv2.cvtColor(framee, cv2.COLOR_BGR2GRAY)  #converting to gray scale
    #frame=cv2.flip(frame,90)
    
 
    output = cv2.Canny(frame,10,250,apertureSize=5, L2gradient=True)
    lines = cv2.HoughLines(output,1,np.pi/180,300) # lines are in polar coordinates r and theta 
    
    if lines is not None:
        for r, th in lines[0]:
            a = np.cos(th)
            b = np.sin(th)
            x = a * r 
            y = b * r
            x1 = int(x + 1000*(-b))
            y1 = int(y + 1000*(a))
            x2 = int(x - 1000*(-b))
            y2 = int(y - 1000*(a))
            cv2.line(framee, (x1, y1), (x2, y2), (0, 0, 255), 4)
    cv2.imshow('video1',framee)

    
    if cv2.waitKey(1)==27:
        break
cap.release()        
cv2.destroyAllWindows()        

