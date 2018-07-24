
# coding: utf-8

# In[1]:


import cv2
import numpy as np
from matplotlib import pyplot as plt


# Thersholding .... If pixel value is greater than a threshold value, it is assigned one value (may be white), else it is assigned another value (may be black). The function used is cv2.threshold. 
# 
# First argument is the source image, which should be a grayscale image. 
# 
# Second argument is the threshold value which is used to classify the pixel values. 
# 
# Third argument is the maxVal which represents the value to be given if pixel value is more than (sometimes less than) the threshold value. 
# 
# OpenCV provides different styles of thresholding and it is decided by the fourth parameter of the function. 
# 
# 
# Different types are:
# 
# 
# • cv2.THRESH_BINARY
# 
# • cv2.THRESH_BINARY_INV
# 
# • cv2.THRESH_TRUNC
# 
# • cv2.THRESH_TOZERO
# 
# • cv2.THRESH_TOZERO_INV

# In[2]:



img=cv2.imread('/Users/chand/Downloads/fox.jpg',0)

ret,thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
ret,thresh2 = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
ret,thresh3 = cv2.threshold(img,127,255,cv2.THRESH_TRUNC)
ret,thresh4 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO)
ret,thresh5 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)

titles = ['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]




# # showing the images through Matplot

# In[3]:


for i in range(6): 
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray') 
    plt.title(titles[i]) 
    plt.xticks([]),plt.yticks([])
plt.show()


# # showing the images through OpenCV

# In[4]:


cv2.imshow('THRESH_BINARY',thresh1)
cv2.imshow('THRESH_BINARY_INV',thresh2)
cv2.imshow('THRESH_TRUNC',thresh3)
cv2.imshow('THRESH_TOZERO',thresh4)
cv2.imshow('THRESH_TOZERO_INV',thresh5)
cv2.waitKey(0)
cv2.destroyAllWindows()


# Adaptive thersholding : In this, the algorithm calculate the threshold for a small regions of the image. So we get different thresholds for different regions of the same image and it gives us better results for images with varying illumination.

# In[12]:


img=cv2.imread('/Users/chand/Downloads/seagull.jpg',0)


# 
# 
# cv2.ADAPTIVE_THRESH_MEAN_C : threshold value is the mean of neighbourhood area
#     
# cv2.ADAPTIVE_THRESH_GAUSSIAN_C : threshold value is the weighted sum of neighbourhood values 
#                                   where weights are a gaussian window
#         
# Block Size - size of neighbour data
# 
# C - constant subtracted from the mean or weighted mean calculated.
# 
# 

# In[13]:


block_size = 503
constant = 2
th1 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, block_size, constant)
th2 = cv2.adaptiveThreshold (img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, block_size, constant)


# In[7]:


output = [img, th1, th2]
    
titles = ['Original', 'Mean Adaptive', 'Gaussian Adaptive']
    
for i in range(3):
    plt.subplot(1, 3, i+1)
    plt.imshow(output[i],cmap='gray')
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])

plt.show()  


# In[9]:


# showing the images through OpenCV


# In[8]:


cv2.imshow('Mean Adaptive',th1)
cv2.imshow('Guassian Adaptive',th2)
cv2.waitKey(0)
cv2.destroyAllWindows()

