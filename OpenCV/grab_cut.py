
# coding: utf-8

# In[57]:


import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('/Users/chand/Downloads/fox.jpg')
mask = np.zeros(img.shape[:2],np.uint8)

bgdModel = np.zeros((1,65),np.float64)
fgdModel = np.zeros((1,65),np.float64)


thresh=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

edge=cv2.Canny(thresh,30,70)
#kernel = np.ones((3,3), np.uint8) 
#img_dil = cv2.dilate(edge, kernel, iterations=1) 
img1, ctrs,hier = cv2.findContours(edge, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)


area=0
for ctr in ctrs:
    max = cv2.contourArea(ctr)
    if area<max:
        area=max
        

for ctr in ctrs:
    if cv2.contourArea(ctr)<area-100:
        continue
    
    (x,y,w,h) = cv2.boundingRect(ctr)
    #cv2.rectangle(img, (x,y), (x+w,y+h), (255, 0, 0), 2)
    #rect=(x,y,w,h) 
    
#cv2.drawContours(img, ctrs, -1,(0,0,255),3)






cv2.grabCut(img,mask,(x-50,y-50,x+w+30,y+h+30),bgdModel,fgdModel,5,cv2.GC_INIT_WITH_RECT)
mask2 = np.where((mask==2)|(mask==0),0,1).astype('uint8')
img = img*mask2[:,:,np.newaxis]

#plt.imshow(img),plt.colorbar(),plt.show()
cv2.imshow("rect",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

