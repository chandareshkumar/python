
# coding: utf-8

# In[26]:


import cv2
import numpy as np
from PIL import Image


# In[28]:


face_cascade = cv2.CascadeClassifier('/Users/chand/Downloads/haarcascade_frontalface_default.xml')


# In[38]:


Id=input('enter your id: ')
sampleNum=21


# In[39]:


font = cv2.FONT_HERSHEY_SIMPLEX

cap = cv2.VideoCapture(0) 
while(cap.isOpened()):
	ret, frame = cap.read()
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	gray = cv2.flip(gray,90)
	faces = face_cascade.detectMultiScale(gray, 1.3, 5)



     
	for (x,y,w,h) in faces:

     
	    cv2.rectangle(gray,(x,y),(x+w,y+h),(255,0,0),2)
	    #cv2.putText(gray, str(face),(900,160),font,4,(0,0,0),4,cv2.LINE_AA)        
	    roi_gray = gray[y:y+h, x:x+w]
	    sampleNum = sampleNum+1

	    cv2.imwrite("/Users/chand/Documents/Dataset/user."+Id+'.'+str(sampleNum)+".jpg",gray[y:y+h,x:x+w])
	    cv2.imshow('frame',gray)       


    
	if cv2.waitKey(1) & 0xFF == ord('q'):
	    break
	elif sampleNum>40:
	    break        

cap.release()
cv2.destroyAllWindows()



# In[19]:


cap.release()

