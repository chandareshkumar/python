
# coding: utf-8

# In[2]:



import numpy as np
import cv2
import matplotlib.pyplot as plt

img1 = cv2.imread('/Users/chand/Downloads/ball.jpg',0)
img2 = cv2.imread('/Users/chand/Downloads/balls.jpg',0)

orb = cv2.ORB_create()

kp1, des1 = orb.detectAndCompute(img1,None)
kp2, des2 = orb.detectAndCompute(img2,None)

bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

matches = bf.match(des1,des2)
matches = sorted(matches, key = lambda x:x.distance)

img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:],None, flags=2)

cv2.imshow('image',img3)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[ ]:


cap.release()

