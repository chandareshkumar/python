
# coding: utf-8

# In[1]:


import cv2
import numpy as np


# In[2]:


img = cv2.imread('/Users/chand/Downloads/golf.jpg')


# In[3]:


px = img[100,100]


# In[4]:


print(px)


# In[5]:


ball = img[285:602,141:496]
img[285:602, 596:951] = ball


# In[ ]:


cv2.namedWindow("img")
cv2.imshow("img",img)
k=cv2.waitKey()

while (1):
    if k== ord('x'):
        break
cv2.destroyAllWindows()        

