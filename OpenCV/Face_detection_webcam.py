



import numpy as np
import cv2





face_cascade = cv2.CascadeClassifier('/Users/chand/Downloads/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('/Users/chand/Downloads/haarcascade_eye.xml')

font = cv2.FONT_HERSHEY_SIMPLEX

cap = cv2.VideoCapture(0) 
while(cap.isOpened()):
	ret, frame = cap.read()
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	gray = cv2.flip(gray,90)
	faces = face_cascade.detectMultiScale(gray, 1.3, 5)

	face=len(faces)

     
	for (x,y,w,h) in faces:
	    #print(len(faces))
     
	    cv2.rectangle(gray,(x,y),(x+w,y+h),(255,0,0),2)
	    cv2.putText(gray, str(face),(900,160),font,4,(0,0,0),4,cv2.LINE_AA)   # displaying the count     
	    roi_gray = gray[y:y+h, x:x+w]

	    eyes = eye_cascade.detectMultiScale(roi_gray)
	    for (ex,ey,ew,eh) in eyes:
	        cv2.rectangle(roi_gray,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)






	cv2.imshow('frame',gray)
	if cv2.waitKey(1) & 0xFF == ord('q'):
	    break
cap.release()
cv2.destroyAllWindows()

