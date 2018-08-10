
# coding: utf-8

# In[1]:


import cv2


# In[46]:


img=cv2.imread("/Users/chand/Downloads/shapes.jpg")


# In[47]:


gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
blur=cv2.GaussianBlur(gray,(5,5),0)  # removing high frequency components
ret,thresh=cv2.threshold(blur, 60,255, cv2.THRESH_BINARY)


# In[48]:


#finding edges


# In[49]:


edges=cv2.Canny(thresh,20,60,3)


# In[50]:


#finding contours


# In[51]:


i,ctrs,hier=cv2.findContours(edges,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)


# In[52]:


for c in ctrs:
    if cv2.contourArea(c) < 200:
        continue
    M = cv2.moments(c)      #finding the moments of shape    
    cX = int(M["m10"] / M["m00"])
    cY = int(M["m01"] / M["m00"])
    cv2.drawContours(img, [c], -1, (0, 255, 0), 2)
    cv2.circle(img, (cX, cY), 7, (255, 255, 255), -1)
    cv2.putText(img, "center", (cX - 20, cY - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
    
    


# In[53]:


cv2.imshow("shape",img)
cv2.waitKey(0)

