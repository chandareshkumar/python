
# coding: utf-8

# In[2]:


import cv2,os
import numpy as np
from PIL import Image


# In[3]:


cv2.__version__


# In[27]:


faceCascade = cv2.CascadeClassifier('/Users/chand/Downloads/haarcascade_frontalface_default.xml')
recognizer = cv2.face.LBPHFaceRecognizer_create()

recognizer.read('/Users/chand/Documents/trainer//trainner.yml')


# In[30]:


cam = cv2.VideoCapture(0)
font= cv2.FONT_HERSHEY_SIMPLEX
while True:
    ret, im =cam.read()
    gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    faces=faceCascade.detectMultiScale(gray, 1.2,5)
    for(x,y,w,h) in faces:
        cv2.rectangle(im,(x,y),(x+w,y+h),(0,255,0),2)
        Id, conf = recognizer.predict(gray[y:y+h,x:x+w])
        if(conf<50):
            if(Id==1):
                Id="Chand"
            elif(Id==2):
                Id="Vijay"
        else:
            Id="Unknown"
        
        cv2.putText(im, str(Id), (x,y+h),font,4,(255,255,0),4,cv2.LINE_AA)       

    cv2.imshow('im',im) 
    if cv2.waitKey(10) & 0xFF==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()


# In[20]:


cam.release()
cv2.destroyAllWindows()

