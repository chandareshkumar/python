
# coding: utf-8

# 
# param1 – First method-specific parameter. In case of CV_HOUGH_GRADIENT , it is the higher threshold of the two passed to the Canny() edge detector (the lower one is twice smaller).
# param2 – Second method-specific parameter. In case of CV_HOUGH_GRADIENT , it is the accumulator threshold for the circle centers at the detection stage. 
# The smaller it is, the more false circles may be detected. Circles, corresponding to the larger accumulator values, will be returned first.
# 
# 

# In[15]:


import cv2
import numpy as np
img = cv2.imread('/Users/chand/Downloads/coins.png',0)
img = cv2.medianBlur(img,3)
ret,img1 = cv2.threshold(img,145,255,cv2.THRESH_BINARY_INV)


img = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)

circles = cv2.HoughCircles(img1,method=cv2.HOUGH_GRADIENT,dp=1,minDist=20,
                            param1=33,param2=25,minRadius=0,maxRadius=0)

#method = Detection method to use.Currently, the only implemented method is CV_HOUGH_GRADIENT

#For example, if dp=1 , the accumulator has the same resolution as the input image. 
#If dp=2 ,the accumulator has half as big width and height.


for i in circles[0,:]:
    # draw the outer circle
    cv2.circle(img,(i[0],i[1]),i[2],(0,255,0),2) # draw the center of the circle 
    cv2.circle(img,(i[0],i[1]),2,(0,0,255),3)
cv2.imshow('detected circles',img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[7]:


capture.release()

