import numpy as np
import cv2


params = cv2.SimpleBlobDetector_Params()
params.filterByArea=True
params.minArea = 100

# Filter by Circularity
params.filterByCircularity = True
params.maxCircularity = 0.9
 
detector = cv2.SimpleBlobDetector_create(params)
     


# Read image
im = cv2.imread("shapes.jpg")
#im = cv2.GaussianBlur(im,(5,5),0)



keypoints = detector.detect(im)

im_with_keypoints = cv2.drawKeypoints(im, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
 

#cv2.imshow("thresh", thresh)
cv2.imshow("blobs", im_with_keypoints)

if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()




