
# coding: utf-8

# In[7]:


import cv2
import numpy as np


# In[8]:


cap=cv2.VideoCapture(0)

while cap.isOpened():

    
    ret, frame = cap.read()    #reading the frame
    

    frame=cv2.flip(frame,90)
    B, G, R = cv2.split(frame)    #splitting the channels
    
    M = np.maximum(np.maximum(R, G), B) 
    
    R[R < M] = 0
    
    G[G < M] = 0
    
    B[B < M] = 0
    
    frame = cv2.merge((B, G, R))

    


    cv2.imshow('video1',frame)

    
    if cv2.waitKey(1)==27:
        break


# In[9]:


cap.release()
cv2.destroyAllWindows()

