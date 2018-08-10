
# coding: utf-8

# In[33]:


import cv2


# In[66]:


img=cv2.imread("/Users/chand/Downloads/shapes.jpg")


# In[67]:


gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
blur=cv2.GaussianBlur(gray,(5,5),0)  # removing high frequency components
ret,thresh=cv2.threshold(blur, 60,255, cv2.THRESH_BINARY)


# In[68]:


#finding edges


# In[69]:


edges=cv2.Canny(thresh,20,60,3)


# In[70]:


#finding contours


# In[71]:


i,ctrs,hier=cv2.findContours(edges,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)


# In[72]:


def shape_detection(c) :
    
    shape = "unidentified"
    peri = cv2.arcLength(c, True)          # True refers closed geometry
    approx = cv2.approxPolyDP(c, 0.04 * peri, True)
    
    if len(approx) == 3:
        shape = "triangle"
        
    elif len(approx) == 4:

        (x, y, w, h) = cv2.boundingRect(approx)
        ar = w / float(h)
        shape = "square" if ar >= 0.95 and ar <= 1.05 else "rectangle"
        
    elif len(approx) == 5:
        shape = "pentagon"
        
    else:
        shape = "circle"

    
    
    return shape


# In[73]:


for c in ctrs:
    if cv2.contourArea(c) < 200:
        continue
    shape = shape_detection(c)   
    M = cv2.moments(c)      #finding the moments of shape    
    cX = int(M["m10"] / M["m00"])
    cY = int(M["m01"] / M["m00"])
    cv2.drawContours(img, [c], -1, (0, 255, 0), 2)
    cv2.circle(img, (cX, cY), 7, (255, 255, 255), -1)
    cv2.putText(img, str(shape), (cX - 20, cY - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
    
    


# In[ ]:


cv2.imshow("shape",img)
cv2.waitKey(0)


# In[2]:


# approxPolyDP Based on Ramer–Douglas–Peucker algorithm


# In[14]:




