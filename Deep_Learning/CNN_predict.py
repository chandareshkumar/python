from keras.preprocessing import image
import numpy as np
from keras.models import model_from_json



json_file = open('/Users/chand/Downloads/Convolutional_Neural_Networks/classifier.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
# load weights into new model
loaded_model.load_weights("/Users/chand/Downloads/Convolutional_Neural_Networks/model.h5")
print("Loaded model from disk")




test_img = image.load_img('/Users/chand/Downloads/Convolutional_Neural_Networks/dataset/single_prediction/cats-pictures-3.jpg', target_size=(64,64))
test_img = image.img_to_array(test_img)

# adding the fourth dimension the batch size
test_img = np.expand_dims(test_img, axis=0)

result = loaded_model.predict_classes(test_img)

#print("training_set.class_indices", training_set.class_indices)



print("prediction", result)    