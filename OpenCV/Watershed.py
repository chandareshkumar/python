
# coding: utf-8

# In[12]:



import numpy as np
import matplotlib.pyplot as plt
from skimage.segmentation import quickshift,felzenszwalb,slic
from skimage.morphology import watershed
from skimage.feature import peak_local_max
from scipy import ndimage
from skimage.segmentation import mark_boundaries
import cv2
from skimage.measure import regionprops
import math
from skimage.filters import threshold_otsu


# In[13]:


img = cv2.imread('/Users/chand/Downloads/coins_combined.jpg')
img = cv2.resize(img, (640,480))


gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

gray = cv2.GaussianBlur(gray,(25,25),0)

thresh = threshold_otsu(gray)
thresh = cv2.threshold(gray, 0, 255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]


cv2.imshow("Thresh", thresh)

    



# In[14]:


# compute the exact Euclidean distance from every binary
# pixel to the nearest zero pixel, then find peaks in this
# distance map


# In[15]:


D = ndimage.distance_transform_edt(thresh)
localMax = peak_local_max(D, indices=False, min_distance=20,
	labels=thresh)


# In[16]:


# perform a connected component analysis on the local peaks,
# using 8-connectivity, then appy the Watershed algorithm


# In[17]:


markers = ndimage.label(localMax, structure=np.ones((3, 3)))[0]
labels = watershed(-D, markers, mask=thresh)
print("[INFO] {} unique segments found".format(len(np.unique(labels)) - 1))


# In[18]:


# loop over the unique labels returned by the Watershed
# algorithm


# In[19]:


for label in np.unique(labels):
	# if the label is zero, we are examining the 'background'
	# so simply ignore it
	if label == 0:
		continue
 
	# otherwise, allocate memory for the label region and draw
	# it on the mask
	mask = np.zeros(gray.shape, dtype="uint8")
	mask[labels == label] = 255
 
	# detect contours in the mask and grab the largest one
	cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
		cv2.CHAIN_APPROX_SIMPLE)[-2]
	c = max(cnts, key=cv2.contourArea)
 
	# draw a circle enclosing the object
	((x, y), r) = cv2.minEnclosingCircle(c)
	cv2.circle(img, (int(x), int(y)), int(r), (0, 255, 0), 2)
	cv2.putText(img, "#{}".format(label), (int(x) - 10, int(y)),
		cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)


# In[20]:


cv2.imshow("result", img)

if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()

