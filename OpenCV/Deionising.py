
# coding: utf-8

# Image Denoising in OpenCV
# OpenCV provides four variations of this technique.
# 
# 1. cv2.fastNlMeansDenoising() - works with a single grayscale images
# 2. cv2.fastNlMeansDenoisingColored() - works with a color image.
# 3. cv2.fastNlMeansDenoisingMulti() - works with image sequence captured in short period of time (grayscale images)
# 4. cv2.fastNlMeansDenoisingColoredMulti() - same as above, but for color images. Common arguments are:
#     
# • h : parameter deciding filter strength. Higher h value removes noise better, 
#     but removes details of image also. (10 is ok)
#     
# • hForColorComponents : same as h, but for color images only. (normally same as h)
#     
# • templateWindowSize : should be odd. (recommended 7)
#     
# • searchWindowSize : should be odd. (recommended 21)

# In[1]:


import numpy as np
import cv2
from matplotlib import pyplot as plt
img = cv2.imread('/Users/chand/Downloads/noise.png')
dst = cv2.fastNlMeansDenoisingColored(img,None,10,10,7,21)

cv2.imshow('Original Image',img)
cv2.imshow('Deionised Image',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()

