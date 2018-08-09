
# coding: utf-8

# In[15]:


import cv2
import matplotlib.pyplot as plt
import numpy as np


# In[ ]:


# Histogram calculates the pixel frequency of intensities


# In[24]:


impath = "/Users/chand/Downloads/fox.jpg"
img = cv2.imread(impath, 1)
  
plt.subplot(1, 2, 1)
plt.imshow(img)
plt.title('Image')
plt.xticks([])
plt.yticks([])

plt.subplot(1, 2, 2)
hist,bins = np.histogram(img.ravel(), 256, [0, 255])    # image must be flattened to single dimension
plt.title('Histogram')
plt.plot(hist)
plt.xlim(xmin=0, xmax=256)
#plt.ylim(ymin=0,ymax=7000)# limiting the values
plt.show()


# In[25]:


img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)


# In[26]:


R,G,B = cv2.split(img)


# In[27]:


plt.subplot(1, 2, 2)
hist,bins=np.histogram(R.ravel(), 256, [0, 255])    # image must be flattened to single dimension
plt.title('R channel Histogram')
plt.xlim(xmin=0, xmax=256)
plt.plot(hist)
plt.show()


# In[28]:


plt.subplot(1, 2, 2)
hist,bins=np.histogram(G.ravel(), 256, [0, 255])    # image must be flattened to single dimension
plt.title('Green channel Histogram')
plt.xlim(xmin=0, xmax=256)
plt.plot(hist)
plt.show()


# In[29]:


plt.subplot(1, 2, 2)
hist,bins=np.histogram(B.ravel(), 256, [0, 255])    # image must be flattened to single dimension
plt.title('Blue channel Histogram')
plt.xlim(xmin=0, xmax=256)
plt.plot(hist)
plt.show()

