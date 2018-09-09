
# coding: utf-8

# In[1]:


import numpy as np
import cv2
img = cv2.imread('/Users/chand/Downloads/fox.jpg')
Z = img.reshape((-1,3))
# convert to np.float32
Z = np.float32(Z)
# define criteria, number of clusters(K) and apply kmeans()
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)

# criteria [It is the iteration termination criteria.When this criteria is satisfied,algorithm iteration stops.Actually, it should be a tuple of 3 parameters.They are( type, max_iter, epsilon ):]

• 3.a - type of termination criteria [It has 3 flags as below:] 

cv2.TERM_CRITERIA_EPS - stop the algorithm iteration if specified accuracy, epsilon, is reached. cv2.TERM_CRITERIA_MAX_ITER - stop the algorithm after the specified number of iterations, max_iter. cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER - stop the iteration when any of the above condition is met.

• 3.b - max_iter - An integer specifying maximum number of iterations.
• 3.c - epsilon - Required accuracy
# In[4]:


K=8

ret,label,center=cv2.kmeans(Z,K,None,criteria,10,cv2.KMEANS_RANDOM_CENTERS)
# Now convert back into uint8, and make original image
center = np.uint8(center)
res = center[label.flatten()]
res2 = res.reshape((img.shape))
cv2.imshow('Quantized Image',res2)
cv2.imshow('Original Image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

