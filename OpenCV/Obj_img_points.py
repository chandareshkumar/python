
# coding: utf-8

# # Camera calibration

# In[1]:


import numpy as np
import cv2
import glob
import os
# termination criteria

criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)
# prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)



'''criteria [It is the iteration termination criteria.When this criteria is satisfied,
 algorithm iteration stops.Actually, it should be a tuple of 3 parameters.
 They are( type, max_iter, epsilon ):]

• 3.a - type of termination criteria 
        [It has 3 flags as below:] 
        cv2.TERM_CRITERIA_EPS - stop the algorithm iteration 
        if specified accuracy, epsilon, is reached.
         cv2.TERM_CRITERIA_MAX_ITER - stop the algorithm after the specified number of iterations, 
         max_iter. cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER - 
         stop the iteration when any of the above condition is met.

• 3.b - max_iter - An integer specifying maximum number of iterations.
• 3.c - epsilon - Required accuracy

'''


objp = np.zeros((6*7,3), np.float32)
objp[:,:2] = np.mgrid[0:7,0:6].T.reshape(-1,2)

# Arrays to store object points and image points from all the images. 
objpoints = [] # 3d point in real world space
imgpoints = [] # 2d points in image plane.

path='/Users/chand/Downloads/chessboard'
images=[os.path.join(path,f) for f in os.listdir(path)] 



for fname in images:
    if fname=='/Users/chand/Downloads/chessboard/.DS_Store':
        continue
    img = cv2.imread(fname)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    # Find the chess board corners
    ret, corners = cv2.findChessboardCorners(gray, (7,6),None)
    # If found, add object points, image points (after refining them)
    if ret == True: 
        objpoints.append(objp)
        corners2 = cv2.cornerSubPix(gray,corners,(11,11),(-1,-1),criteria)
        imgpoints.append(corners2)
        # Draw and display the corners
        img = cv2.drawChessboardCorners(img, (7,6), corners2,ret)
        cv2.imshow('img',img)
        cv2.waitKey(500)
cv2.destroyAllWindows()

