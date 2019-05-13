import numpy as np
import cv2
from gender_prediction import gender_pred
import random





face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

font = cv2.FONT_HERSHEY_SIMPLEX


def image_crop(img):

	roi_gray=[]

	img =cv2.imread(img)
	img1=img.copy()
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)




	faces = face_cascade.detectMultiScale(gray, 1.3, 5)

	face=len(faces)

     
	for (x,y,w,h) in faces:
	    #print(len(faces))
     
	    cv2.rectangle(img,(x,y-20),(x+w,y+h),(0,255,0),3)
	  
	    roi = img1[y-20:y+h, x:x+w]



	return img,roi ,x,y



	



	

img,cropped,x,y=image_crop("/Users/chand/Downloads/dhoni.jpg")

ran=str(random.randint(1,10000))
path="/Users/chand/Documents/Projects/face_detection/crop/cropped_img"+ran+".jpg"

cv2.imwrite(path,cropped)


classes,prob=gender_pred(path)

if classes == 1:

	cv2.putText(img, str("Woman"),(x-50,y-40),font,1,(0,255,0),2,cv2.LINE_AA)  

	cv2.putText(img, str(prob[0][1]),(x+120,y-40),font,1,(0,255,0),2,cv2.LINE_AA)          



	print("Woman  ", prob[0][1])

else:
	cv2.putText(img, str("Man"),(x-20,y-40),font,1,(0,255,0),2,cv2.LINE_AA)
	cv2.putText(img, str(prob[0][0]),(x+120,y-40),font,1,(0,255,0),2,cv2.LINE_AA)                
	print("Man  ", prob[0][0] )

while(1):
	cv2.imshow("Original image",img)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
cv2.destroyAllWindows()







