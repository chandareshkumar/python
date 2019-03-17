from keras.preprocessing import image
import numpy as np
from keras.models import model_from_json
import cv2


json_file = open('/Users/chand/Documents/Projects/face_detection/gender_classifier.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
# load weights into new model
loaded_model.load_weights("/Users/chand/Documents/Projects/face_detection/gender_classifier.h5")
print("Loaded model from disk")




def gender_pred(img):



	test_img = image.load_img(img, target_size=(96,96))




	test_img = image.img_to_array(test_img)

	test_img = np.array(test_img, dtype="float") / 255.0
	# adding the fourth dimension the batch size
	test_img = np.expand_dims(test_img, axis=0)



	classes = loaded_model.predict_classes(test_img)
	prob = loaded_model.predict(test_img)

	return classes, prob







