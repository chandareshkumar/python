
# coding: utf-8

# In[15]:


import cv2
import matplotlib.pyplot as plt
import numpy as np


# In[ ]:


# Histogram calculates the pixel frequency of intensities


# In[66]:


impath = "/Users/chand/Downloads/fox.jpg"
img = cv2.imread(impath,0)


#img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

# Histogram equalization can also be done to individual channel

eq=cv2.equalizeHist(img)

# Contrast Limited Histogram Equalization

# Parameters are optional

cl=cv2.createCLAHE()
clache = cl.apply(img)

cv2.imshow("equalized",eq)
cv2.imshow("Original",img)
cv2.imshow("CLACHE",clache)
cv2.waitKey(0)







