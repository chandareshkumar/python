
# coding: utf-8

# In[1]:


import cv2
import numpy as np


# In[ ]:


cap = cv2.VideoCapture(0)


# In[12]:


while cap.isOpened():

    
    ret, frame = cap.read()    #reading the frame
    ret,thresh1 = cv2.threshold(frame,127,255,cv2.THRESH_BINARY )
    ret,thresh2 = cv2.threshold(frame,127,255,cv2.THRESH_BINARY_INV )
    ret,thresh3 = cv2.threshold(frame,127,255,cv2.THRESH_TRUNC )
    ret,thresh4 = cv2.threshold(frame,127,255,cv2.THRESH_TOZERO )
    ret,thresh5 = cv2.threshold(frame,127,255,cv2.THRESH_TOZERO_INV)    

        
    cv2.imshow('THRESH_BINARY',thresh1)
    cv2.imshow('THRESH_BINARY_INV',thresh2)
    cv2.imshow('THRESH_TRUNC',thresh3)
    cv2.imshow('THRESH_TOZERO',thresh4)
    cv2.imshow('THRESH_TOZERO_INV',thresh5)

    
    if cv2.waitKey(1)==27:
        break




cv2.destroyAllWindows()    
cap.release()


