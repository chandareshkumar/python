
# coding: utf-8

# In[1]:


import cv2
import numpy as np


# In[8]:


blue = np.uint8([[[255,0,0 ]]])


# In[11]:


blue=cv2.cvtColor(blue,cv2.COLOR_BGR2HSV)


# In[12]:


blue


# In[4]:


cap = cv2.VideoCapture(0) 

while(cap.isOpened()):
	ret, frame = cap.read()
    
	#gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
	# define range of blue color in HSV
    
	lower_blue = np.array([110,50,50])
	upper_blue = np.array([130,255,255])
    
	# Threshold the HSV image to get only blue colors
    
	mask = cv2.inRange(hsv, lower_blue, upper_blue) # Bitwise-AND mask and original image
	res = cv2.bitwise_and(frame,frame, mask= mask)
	cv2.imshow('frame',frame) 
	cv2.imshow('mask',mask) 
	cv2.imshow('res',res) 
	k = cv2.waitKey(5) & 0xFF 
	if k == 27:
	    break
cap.release()        

