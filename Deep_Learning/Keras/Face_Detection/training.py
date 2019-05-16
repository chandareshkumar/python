

# Importing the Keras libraries and packages
from keras.models import Sequential
from keras.layers import Conv2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense
from keras.preprocessing import image
import numpy as np
from keras.models import model_from_json


# Initialising the CNN
classifier = Sequential()

# Conv2D("No of filter", "shape of filter","input_shape","activation_func", border_mode="same"(Default))

# Step 1 - Convolution
classifier.add(Conv2D(32, (3, 3), input_shape = (64, 64, 3), activation = 'relu'))

# Step 2 - Pooling
classifier.add(MaxPooling2D(pool_size = (2, 2)))

# Adding a second convolutional layer
classifier.add(Conv2D(32, (3, 3), activation = 'relu'))
classifier.add(MaxPooling2D(pool_size = (2, 2)))

# Step 3 - Flattening
classifier.add(Flatten())

# Step 4 - Full connection
classifier.add(Dense(units = 128, activation = 'relu'))
classifier.add(Dense(units = 1, activation = 'sigmoid'))

# Compiling the CNN

classifier.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])
# Part 2 - Fitting the CNN to the images

from keras.preprocessing.image import ImageDataGenerator

train_datagen = ImageDataGenerator(rescale = 1./255,
                                   shear_range = 0.2,
                                   zoom_range = 0.2,
                                   horizontal_flip = True)

test_datagen = ImageDataGenerator(rescale = 1./255)

training_set = train_datagen.flow_from_directory("/Users/chand/Documents/git/python/Deep_Learning/Keras/Face_Detection/Face_images/",
                                                 target_size = (64, 64),
                                                 batch_size = 32,
                                                 class_mode = 'binary')

'''test_set = test_datagen.flow_from_directory('/Users/chand/Downloads/Convolutional_Neural_Networks/dataset/test_set',
                                            target_size = (64, 64),
                                            batch_size = 32,
                                            class_mode = 'binary')'''
label_map = (training_set.class_indices)
label_map = dict((v,k) for k,v in label_map.items())

print("label_map", label_map)

classifier.fit_generator(training_set,
                         steps_per_epoch = 20,
                         epochs = 3,
                         #validation_data = test_set,
                         #validation_steps = 2000
                         )



def save_model(classifier):
	classifier_json = classifier.to_json()
	with open("Face_detection.json", "w") as json_file:
		json_file.write(classifier_json)

# serialize weights to HDF5
	classifier.save_weights("Face_detection.h5")
	print("Saved model to disk")

save_model(classifier)



