



import numpy as np
import keras.models
from keras.models import model_from_json
from scipy.misc import imread, imresize,imshow



json_file = open('/Users/chand/model.json','r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
#load woeights into new model
loaded_model.load_weights("/Users/chand/model.h5")
loaded_model.compile(loss='categorical_crossentropy',optimizer='adam',metrics=['accuracy'])
print("Loaded Model from disk")





#loaded_model.compile(loss='categorical_crossentropy',optimizer='adam',metrics=['accuracy'])





x = imread('/Users/chand/Documents/Python/output.png',mode='L')






x = np.invert(x)




x = imresize(x,(28,28))






x = x.reshape(1,28,28,1)

def prediction(y):

	out = loaded_model._make_predict_function(y)
	print(out)
	print(np.argmax(out,axis=1))
	return out

