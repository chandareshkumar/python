from flask import Flask, render_template,request
from scipy.misc import imsave,imread,imresize
import numpy as np
import matplotlib.pyplot as plt
from keras.models import model_from_json
import keras.models
import re
import base64
import sys
import os
import cv2
from preprocessing import opencv_preprocessing
from load import *
import tensorflow as tf
#import cv2










json_file = open('/Users/chand/model.json','r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)

#load woeights into new model
loaded_model.load_weights("/Users/chand/model.h5")
loaded_model.compile(loss='categorical_crossentropy',optimizer='adam',metrics=['accuracy'])
loaded_model._make_predict_function()
print("Loaded Model from disk1")



app=Flask(__name__)



#decoding an image from base64 into raw representation
def convertImage(imgData1):
	imgstr = re.search(b'base64,(.*)',imgData1).group(1)
	#print(imgstr)
	with open('output.png','wb') as output:
		output.write(base64.b64decode(imgstr))


@app.route('/')
def index():
	#initModel()
	#render out pre-built HTML file right on the index page
	return render_template("index.html")



@app.route('/predict/',methods=['GET','POST'])
def predict():

	imgData = request.get_data()
	#encode it into a suitable format
	convertImage(imgData)
	print("debug")



	y=cv2.imread('/Users/chand/Documents/Python/output.png')

	opencv_preprocessing(y)





	y=cv2.imread('/Users/chand/Documents/pre/output.jpg',0)





	y=y.astype('float32')

	y /= 255

	

	print("the value of output",y)

	y=y.reshape(1,28,28,1)

	
	



	out = loaded_model.predict(y)
	print(out)
	outarg=np.argmax(out,axis=1)

	print(outarg)

	return str(outarg)
	

if __name__ == "__main__":

	port = int(os.environ.get('PORT', 5000))
	#run the app locally on the givn port
	app.run(host='0.0.0.0', port=port,debug=True)
	#optional if we want to run in debugging mode
	#app.run(debug=True)			
