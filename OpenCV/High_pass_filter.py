
# coding: utf-8

# In[3]:


import cv2

import numpy as np



# In[9]:


img=cv2.imread('/Users/chand/Downloads/sudo.png')



# Sobel - first order derivatives based edge detector 
# 
# and the Laplacian 2nd order derivative, so it is extremely sensitive to noise

# In[10]:


cv2.Laplacian()

# cv2.Laplacian(img, depth, kernel size, scale, delta, border_type)


# Sobel operators is a joint Gausssian smoothing plus differentiation operation, so it is more resistant to noise. 
# 
# 
# If ksize = -1, a 3x3 Scharr filter is used which gives better results than 3x3 Sobel filter. 
# 
# 
# 
# dx = 0 and dy = 1 --- detects horizontal edges
# 
# dy = 1 and dx = 0 --- detects vertical edges 

# In[32]:




edge_lap = cv2.Laplacian(img, -1, ksize=29, scale=1, delta=0, borderType=cv2.BORDER_DEFAULT)
                          

edge_sob_x=cv2.Sobel(img, -1, dx=0,dy=1,ksize=5, scale=1, delta=0, borderType=cv2.BORDER_DEFAULT)


edge_sob_y=cv2.Sobel(img, -1, dx=1,dy=0,ksize=5, scale=1, delta=0, 
                          borderType=cv2.BORDER_DEFAULT)

edge_sob = edge_sob_x + edge_sob_y



edge_sch_x=cv2.Scharr(img, -1, dx=0,dy=1, scale=1, delta=0, borderType=cv2.BORDER_DEFAULT)


edge_sch_y=cv2.Scharr(img, -1, dx=1,dy=0, scale=1, delta=0, 
                          borderType=cv2.BORDER_DEFAULT)

edge_sch = edge_sch_x + edge_sch_y


# Black-to-White transition is taken as Positive slope (it has a positive value) 
# 
# while White-to-Black transition is taken as a Negative slope (It has negative value). 
# 
# So when you convert data to np.uint8, all negative slopes are made zero. 
# 
# In simple words, you miss that edge.

# In[ ]:


cv2.imshow('Original image',img)
cv2.imshow('edge_lap',edge_lap)
cv2.imshow('edge_sob_x',edge_sob_x)
cv2.imshow('edge_sob_y',edge_sob_y)
cv2.imshow('edge_sob',edge_sob)

cv2.imshow('edge_sch_x',edge_sch_x)
cv2.imshow('edge_sch_y',edge_sch_y)
cv2.imshow('edge_sch',edge_sch)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[21]:


cv2.destroyAllWindows()

