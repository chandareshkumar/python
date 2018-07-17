
# coding: utf-8

# In[43]:


import numpy as np
import cv2


# In[44]:



img = cv2.imread("/Users/chand/Downloads/golf.jpg")


# In[45]:


img.shape


# Line need to provide starting and ending point   (255,0,0) ---- color of a line 5 -- thickness of a line

# In[46]:


# To Draw a diagonal  line with thickness of 5 px
img = cv2.line(img,(0,0),(872,349),(25,89,90),5)


# In[47]:


#Centre point and radius

#if -1 fills the closed figure


# In[48]:


img = cv2.circle(img,(447,63), 63, (0,255,255), -1)


# In[49]:


img = cv2.line(img,(89,65),(511,127),(255,0,0),5)


# top left starting point and bottom right point should be given , color and thinkness of the border

# In[50]:



img = cv2.rectangle(img,(384,0),(510,128),(0,255,0),4)


# In[51]:


#text, starting point, font, font scale, color, thickness, line type


# In[52]:


font = cv2.FONT_HERSHEY_SIMPLEX
img=cv2.putText(img,'chand',(33,285), font, 1,(255,0,255),4,cv2.LINE_AA)


# In[55]:


#Capturing top left co-ordinates and bottom right coordinates while doing event "Mouse drag"


# In[56]:


def draw_circle(event,x,y,flags,param):
    

    if event == cv2.EVENT_LBUTTONDOWN:
        #print("crop")
        mosx1.append(x)
        mosx1.append(y)
        #print(mosx1)    
    if event == cv2.EVENT_LBUTTONUP:
        #print("cropend")
        mosx1.append(x)
        mosx1.append(y)
        #print(mosx1)


# In[54]:


cv2.imshow('image',img)

mosx1=[]
cv2.setMouseCallback('image',draw_circle)

k = cv2.waitKey(0)


if k == 27: 
    cv2.destroyAllWindows()
elif k == ord('s'): 
    #print(mosx,mosy)
    img=cv2.rectangle(img,(mosx1[0],mosx1[1]),(mosx1[2],mosx1[3]),(0,255,0),3)
    cv2.imshow('image',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
elif k== ord('m'):
    cv2.imshow('imge',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows() 

