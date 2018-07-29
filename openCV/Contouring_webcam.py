
# coding: utf-8

# In[2]:


import cv2
import numpy as np


# # Contour - tracks continuous edges
# 
# The contour retrieval modes are as follows
# 
# cv2.RETR_EXTERNAL
# 
# cv2.RETR_LIST
# 
# cv2.RETR_CCOMP
# 
# cv2.RETR_TREE
# 
# The contour approximation modes are as follows
# 
# cv2.CHAIN_APPROX_NONE
# 
# cv2.CHAIN_APPROX_SIMPLE
# 
# cv2.CHAIN_APPROX_TC89_L1
# 
# cv2.CHAIN_APPROX_TC89_KCOS

# In[13]:


cap=cv2.VideoCapture(0) # opening default camera


while cap.isOpened():

    
    ret, framee = cap.read()    #reading the frame
    
    frame = cv2.cvtColor(framee, cv2.COLOR_BGR2GRAY)  #converting to gray scale
    #frame=cv2.flip(frame,90)
    
    ret,thresh=cv2.threshold(frame,127,255,0)
    img, ctrs,hier = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(framee, ctrs, -1,(0,0,255),3)
    
    cv2.imshow("thers",framee)


    
    if cv2.waitKey(1)==27:
        break
cap.release()        
cv2.destroyAllWindows()        

