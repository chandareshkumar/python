
# coding: utf-8

# In[8]:


import cv2
import numpy as np
from matplotlib import pyplot as plt


# ret val is used for Otsu’s Binarization
# 
# automatically calculates a threshold value from image histogram for a bimodal image
# 
# 
# For threshold value, simply pass zero. 
# 
# Then the algorithm finds the optimal threshold value and returns you as the second output, retVal. 
# 
# If Otsu thresholding is not used, retVal is same as the threshold value you used.
# 
# 

# In[9]:



img=cv2.imread('/Users/chand/Downloads/fox.jpg',0)

ret,thresh1 = cv2.threshold(img,0,255,cv2.THRESH_BINARY +cv2.THRESH_OTSU)
ret,thresh2 = cv2.threshold(img,0,255,cv2.THRESH_BINARY_INV +cv2.THRESH_OTSU)

blur = cv2.GaussianBlur(img,(5,5),0)
ret3,th3 = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

ret,thresh3 = cv2.threshold(img,0,255,cv2.THRESH_TRUNC +cv2.THRESH_OTSU)
ret,thresh4 = cv2.threshold(img,0,255,cv2.THRESH_TOZERO +cv2.THRESH_OTSU)
ret,thresh5 = cv2.threshold(img,0,255,cv2.THRESH_TOZERO_INV+cv2.THRESH_OTSU)

titles = ['Original Image','BINARY','BINARY_INV','BINARY Improvement','TRUNC','TOZERO','TOZERO_INV']
images = [img, thresh1, thresh2, th3,thresh3, thresh4, thresh5]




# # showing the images through Matplot

# In[10]:


for i in range(7): 
    plt.subplot(2,4,i+1),plt.imshow(images[i],'gray') 
    plt.title(titles[i]) 
    plt.xticks([]),plt.yticks([])
plt.show()


# # showing the images through OpenCV

# In[7]:


cv2.imshow('THRESH_BINARY',thresh1)
cv2.imshow('THRESH_BINARY_INV',thresh2)
cv2.imshow('BINARY IMPROVEMENT',th3)
cv2.imshow('THRESH_TRUNC',thresh3)
cv2.imshow('THRESH_TOZERO',thresh4)
cv2.imshow('THRESH_TOZERO_INV',thresh5)
cv2.waitKey(0)
cv2.destroyAllWindows()

