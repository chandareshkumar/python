

import cv2
import numpy as np
from resize import imageprepare
from matplotlib import pyplot as plt
from numpy import array


def opencv_preprocessing(img2):

		





		img=cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)







		ret,thresh = cv2.threshold(img,180,255,cv2.THRESH_BINARY_INV)





		img, ctrs, hierarchy = cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)



		k=np.ones((5,5), np.uint8)
		    

		erosion = cv2.erode(img, k, iterations = 3)
		    
		dilation = cv2.dilate(erosion, k, iterations = 4)



		def img_split(x,y,w,h):
		    X = img2[y:y+h,x:x+w]
		    return X




		for contour in ctrs:
		    (x,y,w,h) = cv2.boundingRect(contour)
		   # cv2.rectangle(img2, (x,y), (x+w,y+h), (255, 255, 255), 2)
		    #Y=img_split(x,y,w,h)
		    Y = img2[y:y+h,x:x+w]
		    Y1 = img2[y:y+h,x:x+w]

		    

		#cv2.imshow("countour",cv2.resize(X,(20,20)))
		#ret,Y=cv2.threshold(Y,180,255,cv2.THRESH_BINARY_INV)

		#Y=cv2.cvtColor(Y,cv2.COLOR_BGR2GRAY)

		Y=np.invert(Y)
		invert=Y
		cv2.imwrite("/Users/chand/Documents/pre/beforeoutput.jpg",Y1)
		cv2.imwrite("/Users/chand/Documents/pre/invert.jpg",invert)

		Y=cv2.resize(Y,(20,20))

	

		


		Y= cv2.copyMakeBorder(Y,4,4,4,4,cv2.BORDER_CONSTANT,value=[0,0,0])




		


		
	

		cv2.imwrite("/Users/chand/Documents/pre/output.jpg",Y)




