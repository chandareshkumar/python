
# coding: utf-8

# In[48]:


import cv2,os
import numpy as np
from PIL import Image


# In[59]:


detector = cv2.CascadeClassifier('/Users/chand/Downloads/haarcascade_frontalface_default.xml')
recognizer = cv2.face.LBPHFaceRecognizer_create()


# In[60]:


path="/Users/chand/Documents/Dataset/"


# In[61]:


def getImagesAndLabels(path):

    imagePaths=[os.path.join(path,f) for f in os.listdir(path)] 

    faceSamples=[]

    Ids=[]

    for imagePath in imagePaths:
        if imagePath=='/Users/chand/Documents/Dataset/.DS_Store':
            continue    
        pilImage=Image.open(imagePath).convert('L')

        imageNp=np.array(pilImage,'uint8')

        Id=int(os.path.split(imagePath)[-1].split(".")[1])

        faces=detector.detectMultiScale(imageNp)

        for (x,y,w,h) in faces:
            faceSamples.append(imageNp[y:y+h,x:x+w])
            Ids.append(Id)
    return faceSamples,Ids


# In[62]:


faces,Ids = getImagesAndLabels(path)
recognizer.train(faces, np.array(Ids))
recognizer.save('/Users/chand/Documents/trainer/trainner.yml')

