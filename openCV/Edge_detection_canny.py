
# coding: utf-8

# In[1]:


import cv2
import numpy as np


# In[ ]:


def nothing(x): 
    pass

cv2.namedWindow('image')

img = cv2.imread('/Users/chand/Downloads/sudo.png',1)


img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


#creating Trackbar

cv2.createTrackbar('Minimum','image',1,255,nothing)
cv2.createTrackbar('Maximum','image',1,255,nothing)







while True: 
    cv2.imshow('image',img)
    
    k = cv2.waitKey(1) & 0xFF 
    if k == 27:
        break
    # get current positions of four trackbars
    r = cv2.getTrackbarPos('Minimum','image')
    g = cv2.getTrackbarPos('Maximum','image')
    
    k = np.array(([-1, -1, -1], [-1, 8, -1], [-1, -1, -1]), np.float32)
    im = cv2.filter2D(img, -1, k)
    
    
    #Minimum and Maximum values are varied dynamically using Trackbar
    
    output_L2grad = cv2.Canny(img,r,g, L2gradient=True)
    output = cv2.Canny(img,r,g, L2gradient=False)
    cv2.imshow('output img',output)
    cv2.imshow('output L2grad',output_L2grad)

cv2.waitKey(0)
cv2.destroyAllWindows()

