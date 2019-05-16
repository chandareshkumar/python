import numpy as np
import cv2
import os
import random


face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier("harcascade_eye.xml")


def find_faces(im,dirname):

	#print(os.getcwd())

	img= cv2.imread(im)

	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	faces = face_cascade.detectMultiScale(gray, 1.2, 5)


	for (x,y,w,h) in faces:

	 
	    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

	    roi_gray = img[y:y+h, x:x+w]



	#os.chdir(os.path.dirname(os.path.dirname(os.path.dirname(im))))

	os.chdir("/Users/chand/Documents/git/python/Deep_Learning/Keras/Face_Detection/Face_images")
	os.makedirs(dirname,mode=0o777,exist_ok=True)
	os.chdir("/Users/chand/Documents/git/python/Deep_Learning/Keras/Face_Detection/Face_images/"+dirname)
	cv2.imwrite(dirname + str(random.randint(1,50))+'.jpg' ,roi_gray )
	    
	'''eyes = eye_cascade.detectMultiScale(roi_gray)
	    for (ex,ey,ew,eh) in eyes:
	        cv2.rectangle(img,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)'''





	    #cv2.imshow('output img',roi_gray)
	    #cv2.waitKey(0)
	    #cv2.destroyAllWindows()


os.chdir("/Users/chand/Documents/git/python/Deep_Learning/Keras/Face_Detection/images/")	

for dir_path, dir_names, file_names in os.walk(os.getcwd()):
	for f in file_names:
		if f=='.DS_Store':
			continue
		else:
			find_faces(str(dir_path) + '/' + str(f), str(dir_path).split('/')[-1] )
		


def find_faces_test(im):

	print("im",im)

	img= cv2.imread(im)

	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	faces = face_cascade.detectMultiScale(gray, 1.2, 5)


	for (x,y,w,h) in faces:

	 
	    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

	    roi_gray = img[y:y+h, x:x+w]

	    os.chdir("/Users/chand/Documents/git/python/Deep_Learning/Keras/Face_Detection/test_images/")	

	    cv2.imwrite("dirname" + '.jpg' ,roi_gray )

	    return "/Users/chand/Documents/git/python/Deep_Learning/Keras/Face_Detection/test_images/dirname.jpg"


