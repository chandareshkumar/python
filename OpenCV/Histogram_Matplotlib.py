
# coding: utf-8

# In[1]:


import cv2
import matplotlib.pyplot as plt


# In[ ]:


# Histogram calculates the pixel frequency of intensities


# In[6]:


impath = "/Users/chand/Downloads/fox.jpg"
img = cv2.imread(impath, 1)
  
plt.subplot(1, 2, 1)
plt.imshow(img)
plt.title('Image')
plt.xticks([])
plt.yticks([])

plt.subplot(1, 2, 2)
plt.hist(img.ravel(), 256, [0, 255])    # image must be flattened to single dimension
plt.title('Histogram')
plt.xlim(xmin=0, xmax=256)   # limiting the values
plt.show()


# In[10]:


img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)


# In[11]:


R,G,B = cv2.split(img)


# In[12]:


plt.subplot(1, 2, 2)
plt.hist(R.ravel(), 256, [0, 255])    # image must be flattened to single dimension
plt.title('R channel Histogram')
plt.xlim(xmin=0, xmax=256)
plt.show()


# In[13]:


plt.subplot(1, 2, 2)
plt.hist(G.ravel(), 256, [0, 255])    # image must be flattened to single dimension
plt.title('G channel Histogram')
plt.xlim(xmin=0, xmax=256)
plt.show()


# In[14]:


plt.subplot(1, 2, 2)
plt.hist(B.ravel(), 256, [0, 255])    # image must be flattened to single dimension
plt.title('B channel Histogram')
plt.xlim(xmin=0, xmax=256)
plt.show()

