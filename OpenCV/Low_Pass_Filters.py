
# coding: utf-8

# In[1]:


import cv2
import random
import numpy as np
from PIL import Image


# In[12]:


img=cv2.imread('/Users/chand/Downloads/pik.jpg')



# Mean filter (rectangular kernel) is optimal for reducing random noise in spatial domain (image space). However Mean filter is the worst filter for frequency domain, with little ability to separate one band of frequencies from another. Gaussian filter has better performance in frequency domain.
Gaussian filters weigh pixels a bell-curve around the center pixel. 
This means that farther pixels get lower weights.

Mean-filter, a.k.a box-filter, just average the pixel values of all neighboring pixels. 

This is equivalent to giving an equal weight to all pixels around the center regardless of the distance 
from the center pixel.

Box-filters can be calculated faster than Gaussian blurring.
# Low Pass filters helps to do
# 
# 1. Blurring
# 2. Denoising
# 3. Smoothing

# In[7]:


noisy = np.zeros(img.shape, np.uint8)   # Black image


# In[8]:


p = 0.004
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        r = random.random()
        if r < p/2:                                          # Adding noise to the image
            noisy[i][j] = [0, 0, 0]
        elif r < p:
            noisy[i][j] = [255, 255, 255]
        else:
            noisy[i][j] = img[i][j]


# In[9]:


box = cv2.boxFilter(noisy, -1, (23, 23))

blur = cv2.blur(noisy, (13, 13))

gaussian = cv2.GaussianBlur(noisy, (23, 23), 0)

denoised = cv2.medianBlur(noisy, 5)



# In[10]:


# Median Blur works better on the salt and pepper noise


# In[11]:


cv2.imshow('Original image',img)
cv2.imshow('salt and pepper',noisy)
cv2.imshow('box',box)
cv2.imshow('blur',blur)
cv2.imshow('denoised',denoised)
cv2.imshow('gaussian',gaussian)
cv2.waitKey(0)
cv2.destroyAllWindows()

