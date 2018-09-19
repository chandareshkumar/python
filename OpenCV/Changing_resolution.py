
# coding: utf-8

# In[2]:


import cv2


# In[3]:


import numpy as np


# In[4]:


img=cv2.imread("/Users/chand/Downloads/fox.jpg")


# In[5]:


type(img)


# In[6]:


for i in range(4):
    img= cv2.pyrDown(img)
    cv2.imshow("Lower Resolution",img)
    k= cv2.waitKey(0)
    if k==27:
        continue

        

        
cv2.destroyAllWindows()        


# In[7]:


for i in range(4):
    img= cv2.pyrUp(img)
    cv2.imshow("Higher Resolution",img)
    k= cv2.waitKey(0)
    if k==27:
        continue


# In[8]:


cv2.destroyAllWindows()        

