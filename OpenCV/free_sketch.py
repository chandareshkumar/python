
# coding: utf-8

# In[120]:


import cv2
import numpy as np


# In[127]:



img = cv2.imread("/Users/chand/Downloads/green.jpg")


# In[122]:


img.shape


# # drawing=true   --if mouse is pressed
# 
# #  Press 'e' to to toggle between draw and erase mode
# # mouse callback function

# In[124]:


drawing = False 
mode = True 


# Capturing mouse event. On first left click draw mode gets enabled. Then two action can be done
# 
# 1. Draw mode
# 2. Erase
# 
# Note : both action does the same thing if you have close look. Only difference here is "draw mode" draws 
# the circle in red,while erase mode draws the circle in green. since background is complete green, 
# the later action work as eraser.
# 
# #Begginer level

# In[128]:


def draw_circle(event,x,y,flags,param): 
    global ix,iy,drawing,mode
    if event == cv2.EVENT_LBUTTONDOWN: 
        drawing = True

    elif event == cv2.EVENT_MOUSEMOVE: 
        if drawing == True:
            if mode == True: 
                cv2.circle(img,(x,y),10,(0,255,0),-1)  #erase was handled here   #draws circle in green
            else: 
                cv2.circle(img,(x,y),5,(0,0,255),-1)   #draw was handled here    #draws circle in red
    


# In[130]:


#Mouse event is tagged to the main window


# In[131]:



cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_circle)
while(1):
    cv2.imshow('image',img)
    k = cv2.waitKey(1) & 0xFF 
    
    if k == ord('e'):
        mode = not mode   #to toggle the mode
        
    elif k == ord('s'): 
        cv2.imwrite('sketch.jpg',img)   #press 's' to save your sketch
        cv2.destroyAllWindows()  
    elif k == 27:
        
        break
cv2.destroyAllWindows()

