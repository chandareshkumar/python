
# coding: utf-8

# In[31]:


import numpy as np
import cv2
cap = cv2.VideoCapture("/Users/chand/Downloads/video/CCTV.mp4")
length = (cap.get(cv2.CAP_PROP_FRAME_COUNT))
print( length )
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3))
fgbg = cv2.bgsegm.createBackgroundSubtractorGMG()
while(1):
    ret, frame = cap.read()

    if not ret:
        break
    frame1 = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frame1 = cv2.blur(frame1, (3,3))   
    fgmask = fgbg.apply(frame1)
    fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel)
    cv2.imshow('frame',fgmask)
    k = cv2.waitKey(60) & 0xff
cap.release()
cv2.destroyAllWindows()

