
# coding: utf-8

# In[15]:


import cv2
import matplotlib.pyplot as plt
import numpy as np


# In[ ]:


# Histogram calculates the pixel frequency of intensities


# In[46]:


impath = "/Users/chand/Downloads/fox.jpg"
img = cv2.imread(impath, 1)


img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

#R,G,B = cv2.split(img) here no need to split the channel


#cv2.CalcHist(img,[index of color],Mask, No of bits, Range)

red = cv2.calcHist([img],[0],None, [256],(0,255))
green = cv2.calcHist([img],[1],None, [256],(0,255))
blue = cv2.calcHist([img],[2],None, [256],(0,255))

plt.subplot(3, 1, 1)
plt.imshow(img)
plt.title('Image')
plt.xticks([])
plt.yticks([])

plt.subplot(3, 1, 2)
plt.title('Red Histogram')
plt.plot(red)
plt.xlim(xmin=0, xmax=256)


plt.subplot(3, 1, 3)
plt.title('Green Histogram')
plt.plot(green)
plt.xlim(xmin=0, xmax=256)


plt.subplot(3, 1, 2 )
plt.plot(blue,color='b')
plt.xlim(xmin=0, xmax=256)


plt.show()

