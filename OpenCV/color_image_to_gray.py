
# coding: utf-8

# In[1]:


import cv2
import os


# In[2]:


cv2.__version__



# In[3]:


img=cv2.imread('/Users/chand/Downloads/2.png',0)


# ord() function in Python. Given a string of length one, return an integer representing the Unicode code point of the character when the argument is a unicode object, or the value of the byte when the argument is an 8-bit string. 

# In[7]:


cv2.imshow('image',img)
k = cv2.waitKey(0)

if k == 27: 
    cv2.destroyAllWindows()
elif k == ord('s'): 
    cv2.imwrite('2.jpg',img)
    cv2.destroyAllWindows()

