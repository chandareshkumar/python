
# coding: utf-8

# In[5]:


import cv2
import numpy as np
from sklearn.externals import joblib
import SUDOKU



ratio2 = 3
kernel_size = 3

lowThreshold = 30
font = cv2.FONT_HERSHEY_SIMPLEX

clf = joblib.load('classifier.pkl')
cv2.namedWindow("SUDOKU Solver")

vc = cv2.VideoCapture(0)
if vc.isOpened(): # try to get the first frame
    rval, frame = vc.read()

else:
    rval = False
while rval:
 # Preprocess image, convert from RGB to Gray
    flag=0
    New_lines=[]
    Points=[]
    lines=None

    
    sudoku1 = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    sudoku1 = cv2.blur(sudoku1, (3,3))
    
    
    # Apply Canny edge detection
    edges = cv2.Canny(sudoku1, lowThreshold, lowThreshold*ratio2, kernel_size)
    # Apply Hough Line Transform, return a list of rho and theta
    
    # cv2.HoughLines(edges_image, rho_resolution , theta_resolution , thresh
    
    lines = cv2.HoughLines(edges, 1, np.pi/180, 200)


        
        
  
    if (lines is not None):
        lines=lines.tolist()
        lines=sorted(lines)

        pos_hori = 0
        pos_vert = 0
        New_lines = []
        Points = []

        for line in lines:
            
         rho,theta = line[0]   
            
         a = np.cos(theta)
         b = np.sin(theta)
         x0 = a*rho
         y0 = b*rho
         x1 = int(x0 + 1000*(-b))
         y1 = int(y0 + 1000*(a))
         x2 = int(x0 - 1000*(-b))
         y2 = int(y0 - 1000*(a))
            
            
         # If b > 0.5, the angle must be greater than 45 degree
        # print(rho)       
        
        
        
         #cv2.line(frame,(x1,y1),(x2,y2),(0,255,255),2)
         # so we consider that line as a vertical line
         if (b>0.5):
          #cv2.line(frame,(x1,y1),(x2,y2),(0,0,255),2)      
          # Check the position
          if((rho-pos_hori)>20):                             #for removing redundant lines
           # Update the position
           pos_hori=rho
           #cv2.line(frame,(x1,y1),(x2,y2),(255,0,255),2)
           New_lines.append([rho,theta, 0])
         else:
          #cv2.line(frame,(x1,y1),(x2,y2),(0,0,255),2)  
          if((rho-pos_vert)>20):                            #for removing redundant lines
           pos_vert=rho
           New_lines.append([rho,theta, 1])

           #cv2.line(frame,(x1,y1),(x2,y2),(255,0,255),2)

    for i in range(len(New_lines)):
        if(New_lines[i][2] == 0):
            for j in range(len(New_lines)):
                if (New_lines[j][2]==1):
                    theta1=New_lines[i][1]
                    theta2=New_lines[j][1]
                    p1=New_lines[i][0]
                    p2=New_lines[j][0]
                    xy = np.array([[np.cos(theta1), np.sin(theta1)], [np.cos(theta2), np.sin(theta2)]])
                    p = np.array([p1,p2])
                    res = np.linalg.solve(xy, p)
                    Points.append(res)

    if(len(Points)==100):
        
                for i in range(0,100):
                    cv2.circle(frame,(int(Points[i][0]),int(Points[i][1])),5, (255,0,255),-1)
                        
                
                board = []
                result=[]
                sudoku1 = cv2.adaptiveThreshold(sudoku1, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV, 101, 1)
                for i in range(0,9):
                    for j in range(0,9):
                        y1=int(Points[j+i*10][1]+5)
                        y2=int(Points[j+i*10+11][1]-5)
                        x1=int(Points[j+i*10][0]+5)
                        x2=int(Points[j+i*10+11][0]-5)
                        cv2.rectangle(frame,(x1,y1),(x2, y2),(0,255,0),2)
                              
                        X = sudoku1[y1:y2,x1:x2]
                        if(X.size!=0):
                            X = cv2.resize(X, (36,36))
                            num = clf.predict(np.reshape(X, (1,-1)))
                            
                            #Collect the result
                            result.append(num)
                            board.append(num)
                            
                if len(result)==81:            
                    
                    result=np.array(result)
                    board=np.array(board)
                    result = np.reshape(result, (9,9))
                    board = np.reshape(board, (9,9))
                    
                
                # Solve the SUDOKU grid
                    if(SUDOKU.SolveSudoku(result)):
                    # If it can solve SUDOKU matrix, show the result
                        for i in range(0,9):
                            for j in range(0,9):
                                if(board[i][j]==0):
                                    cv2.putText(frame,str(result[i][j]),(int(Points[j+i*10+10][0]+15), 
                                                                     int(Points[j+i*10+10][1]-10)),font,1,(225,0,0),2)
                    # Show the result picture
                        cv2.imshow("Result", frame)
    # Show the result 

    cv2.imshow("SUDOKU Solver", frame)
    rval, frame = vc.read()
    key = cv2.waitKey(20)
    if key == 27: # exit on ESC
     break
    
   
vc.release()
cv2.destroyAllWindows()


