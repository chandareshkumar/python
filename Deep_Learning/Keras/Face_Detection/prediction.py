from keras.preprocessing import image
import numpy as np
from keras.models import model_from_json
from face_extraction import find_faces_test



json_file = open('/Users/chand/Documents/git/python/Deep_Learning/Keras/Face_Detection/Face_detection.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
# load weights into new model
loaded_model.load_weights("/Users/chand/Documents/git/python/Deep_Learning/Keras/Face_Detection/Face_detection.h5")
print("Loaded model from disk")


im="/Users/chand/Documents/git/python/Deep_Learning/Keras/Face_Detection/test_images/1.jpeg"

#need to change incase of multiple faces
img=find_faces_test(im)


test_img = image.load_img(img, target_size=(64,64))
test_img = image.img_to_array(test_img)

# adding the fourth dimension the batch size
test_img = np.expand_dims(test_img, axis=0)

result = loaded_model.predict_classes(test_img)

#print("training_set.class_indices", training_set.class_indices)


if result[0][0]==0:
	print("Pika")
else:
	print("Venky")

#print("prediction", result)