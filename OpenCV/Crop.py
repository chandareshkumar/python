
# coding: utf-8

# In[7]:


import cv2


# In[8]:


crop_pt = []


# In[9]:


def crop(event, x, y, flags, param):

	global crop_pt, cropping,clone,flag,image
    
    # flag ==1 tells that cropping has not done and reset is done here using mouse event. 
    #If we dont add this multiple crop section would be shown. 
    #Have better understanding by removing the block.
    
	if flag==1 & event == cv2.EVENT_LBUTTONDOWN:
		image=clone.copy()
		cv2.imshow("image",image)


	if event == cv2.EVENT_LBUTTONDOWN:
		crop_pt = [(x, y)]



    
	elif event == cv2.EVENT_LBUTTONUP:
        

		crop_pt.append((x, y))

		flag=1
		cv2.rectangle(image, crop_pt[0],crop_pt[1],(0,255,0),2)        



# In[10]:


image = cv2.imread("/Users/chand/Downloads/golf.jpg")
clone = image.copy()
i=0
flag=0


# In[11]:



cv2.namedWindow("image")
cv2.setMouseCallback("image", crop)
 
# keep looping until the 'q' key is pressed

while True:

	# display the image 
	cv2.imshow("image", image)
	key = cv2.waitKey(1) & 0xFF
 
	# if the 'r' key is pressed, reset the cropping region
    
	if key == ord("r"):
		image = clone.copy()
		flag=0       
 

	if key == ord("c"):
 
        #assigning the cropped region to roi
    
	    roi = clone[crop_pt[0][1]:crop_pt[1][1], crop_pt[0][0]:crop_pt[1][0]]

        # Making seperate window for cropped section
        
        # For Multiple crops, windows name was changed dynamically
        
	    cv2.imshow("ROI" + str(i), roi)
	    cv2.imwrite("ROI" + str(i)+'.jpg', roi)        

        
	    image=clone.copy()
	    i=i+1
	    flag=0


            
	if key == ord("q"):
		break 

 
# close all open windows
cv2.destroyAllWindows()

