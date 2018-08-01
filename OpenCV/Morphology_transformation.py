
# coding: utf-8

# In[1]:


import cv2
import numpy as np


# 
# Morphological operations are a set of operations that process images based on shapes. They apply a structuring element to an input image and generate an output image.
# The most basic morphological operations are two: Erosion and Dilation
# Basics of Erosion:
# 
# Erodes away the boundaries of foreground object
# Used to diminish the features of an image.

# Basics of Erosion:
# 
# Erodes away the boundaries of foreground object
# Used to diminish the features of an image.
# Working of erosion:
# 
# A kernel(a matrix of odd size(3,5,7) is convolved with the image.
# A pixel in the original image (either 1 or 0) will be considered 1 only if all the pixels under the kernel is 1, otherwise it is eroded (made to zero).
# Thus all the pixels near boundary will be discarded depending upon the size of kernel.
# So the thickness or size of the foreground object decreases or simply white region decreases in the image.
# Basics of dilation:
# 
# Increases the object area
# Used to accentuate features
# 
# 
# Working of dilation:
# 
# A kernel(a matrix of odd size(3,5,7) is convolved with the image
# A pixel element in the original image is ‘1’ if atleast one pixel under the kernel is ‘1’.
# It increases the white region in the image or size of foreground object increases

# In[2]:


cap=cv2.VideoCapture(0)

while cap.isOpened():

    
    ret, frame = cap.read()    #reading the frame
    

    th = 0
    max_val = 255 
    

    
    
    binary = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    ret,binary_inv = cv2.threshold(frame,th,max_val,cv2.THRESH_BINARY_INV)
    
    #k = cv2.getStructuringElement(cv2.MORPH_CROSS,(5, 5))
    
    k=np.ones((5,5), np.uint8)
    
    #print(type(binary_inv))
    erosion = cv2.erode(binary_inv, k, iterations = 3)
    
    dilation = cv2.dilate(binary_inv, k, iterations = 4)
    
    gradient = cv2.morphologyEx(binary_inv, cv2.MORPH_GRADIENT, k)  
    
    # gradient is the difference between erosion and dilation
    


    cv2.imshow('video1',gradient)

    
    if cv2.waitKey(1)==27:
        break
        
cap.release()  
cv2.destroyAllWindows()


# In[26]:


# Morphology transformation on images


# In[10]:


img = cv2.imread("/Users/chand/Downloads/digitRecognition/sudo.png")
ret,binary_inv = cv2.threshold(img,0,255,cv2.THRESH_BINARY_INV)

k=np.ones((5,5), np.uint8)
    

erosion = cv2.erode(binary_inv, k, iterations = 3)
    
dilation = cv2.dilate(binary_inv, k, iterations = 4)
    
gradient = cv2.morphologyEx(binary_inv, cv2.MORPH_GRADIENT, k)  


# In[11]:


cv2.imshow('erosion',erosion)
cv2.imshow('dilation',dilation)
cv2.imshow('gradient',gradient)
cv2.waitKey(0)
cv2.destroyAllWindows()

