
# coding: utf-8

# In[70]:


import numpy as np
import cv2
import os
import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart


# In[71]:


face_cascade = cv2.CascadeClassifier('/Users/chand/Downloads/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('/Users/chand/Downloads/haarcascade_eye.xml')


# In[72]:


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
	    cv2.putText(gray, str(face),(900,160),font,4,(0,0,0),4,cv2.LINE_AA)        
	    roi_gray = gray[y:y+h, x:x+w]

	    eyes = eye_cascade.detectMultiScale(roi_gray)
	    for (ex,ey,ew,eh) in eyes:
	        cv2.rectangle(roi_gray,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)






	cv2.imshow('frame',gray)
	cv2.imwrite('fram.jpg',gray)    
	if cv2.waitKey(1) & 0xFF == ord('q'):
	    break
cap.release()
cv2.destroyAllWindows()


# In[73]:


COMMASPACE = ', '

def main():
    sender = 'sender mail here'
    gmail_password = 'password'
    recipients = ['recepient mail here']
    
    # Create the enclosing (outer) message
    outer = MIMEMultipart()
    outer['Subject'] = 'Footage snapshot'
    outer['To'] = COMMASPACE.join(recipients)
    outer['From'] = sender
    outer.preamble = 'You will not see this in a MIME-aware mail reader.\n'

    # List of attachments
    attachments = ['/Users/chand/fram.jpg']

    # Add the attachments to the message
    for file in attachments:
        try:
            with open(file, 'rb') as fp:
                msg = MIMEBase('application', "octet-stream")
                msg.set_payload(fp.read())
            encoders.encode_base64(msg)
            msg.add_header('Content-Disposition', 'attachment', filename=os.path.basename(file))
            outer.attach(msg)
        except:
            print("Unable to open one of the attachments. Error: ", sys.exc_info()[0])
            raise

    composed = outer.as_string()

    # Send the email
    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as s:
            s.ehlo()
            s.starttls()
            s.ehlo()
            s.login(sender, gmail_password)
            s.sendmail(sender, recipients, composed)
            s.close()
        print("Email sent!")
    except:
        print("Unable to send the email. Error: ", sys.exc_info()[0])
        raise

if __name__ == '__main__':
    main()

