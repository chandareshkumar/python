
# coding: utf-8

# In[1]:


import cv2
import numpy as np



# In[51]:


img = cv2.imread('/Users/chand/Downloads/star.jpeg')
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(img_gray, 127, 255,0)
im,contours,hierarchy = cv2.findContours(thresh,2,1)






# In[ ]:


cv2.drawContours(img, contours, -1, (0, 255, 255), 3)
for cnt in contours:
    # get convex hull
    hull = cv2.convexHull(cnt)
    #defects = cv2.convexityDefects(cnt,hull)
    cv2.drawContours(img, [hull], -1, (0, 0, 255), 2)
    
    x, y, w, h = cv2.boundingRect(cnt)  
    
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)  
    
    rect = cv2.minAreaRect(cnt)   # here getting the minimum rectangle area
    
   # print("rect",rect)
   # print(type(rect))
    
    box = cv2.boxPoints(rect)  #values are float here
    
   # print("box",box)
   # print(type(box))
    
    box = np.int0(box)
    
   # print(type(box))
    #print(box)
    cv2.drawContours(img, [box], 0, (0, 0, 255))
    
    (x, y), radius = cv2.minEnclosingCircle(cnt)
    center = (int(x), int(y))
    radius = int(radius)
    cv2.circle(img, center, radius, (255, 0, 0), 2)

    
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()    

