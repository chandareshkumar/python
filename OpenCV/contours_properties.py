import numpy as np
import cv2


frame = cv2.imread("coins.jpg")


frame = cv2.resize(frame, (640,480))

gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

gray_blur = cv2.GaussianBlur(gray, (15, 15), 0)
thresh = cv2.adaptiveThreshold(gray_blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
	cv2.THRESH_BINARY_INV, 11, 1)

kernel = np.ones((5, 5), np.uint8)
closing = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE,
	kernel, iterations=4)

closing_img = closing.copy()
im2, contours, hierarchy = cv2.findContours(closing_img,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)


font = cv2.FONT_HERSHEY_SIMPLEX


segment_prop = {}
segments = []

for cnt in contours:

    area = cv2.contourArea(cnt)
   
    if area < 1000:
        continue
    
    print(area)
    
    ellipse = cv2.fitEllipse(cnt)
    
    segment_prop['area'] = area
    segment_prop['perimeter'] = perimeter = cv2.arcLength(cnt,True)
    
    x,y,w,h = cv2.boundingRect(cnt)
    segment_prop['aspect_ratio'] = aspect_ratio = float(w)/h
            
    rect_area = w*h
    segment_prop['extent'] = extent = float(area)/rect_area       
                         
    hull = cv2.convexHull(cnt)
    hull_area = cv2.contourArea(hull)
    segment_prop['solidity'] = solidity = float(area)/hull_area
                
    segments.append(segment_prop)
         
    text = round(segment_prop['extent'],3)
    
    cv2.putText(frame,str(text),(x,y), font, 1,(255,255,255),2,cv2.LINE_AA)
    cv2.ellipse(frame, ellipse, (0,255,0), 2)


del segment_prop

cv2.imshow("Morphological Closing", closing)
cv2.imshow('Contours', frame)

if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()




