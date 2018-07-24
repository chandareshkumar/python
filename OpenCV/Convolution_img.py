
# coding: utf-8

# In[48]:


import cv2


# In[49]:



img = cv2.imread('/Users/chand/Downloads/fox.jpg',1)


img1 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    
#k = np.array(np.ones((11, 11), np.float32))/121
    
k1 = np.array(([-1, -1, -1], [-1, 8, -1], [-1, -1, -1]), np.float32)
 
# sharpen    
k = np.array(([0, -1, 0], [-1, 5, -1], [0, -1, 0]), np.float32)
    
k2 = np.array(([0, -1, 0], [-1, 4, -1], [0, -1, 0]), np.float32)

#Blurring
k3= np.array(np.ones((11,11),np.float32)/121)

output = cv2.filter2D(img1, -1, k3)

#output = cv2.Canny(output,30,600)

cv2.imshow('Original img',img)
cv2.imshow('output img',output)
cv2.waitKey(0)
cv2.destroyAllWindows()


