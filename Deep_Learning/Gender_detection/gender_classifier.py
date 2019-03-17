import matplotlib
matplotlib.use("Agg")
from keras.preprocessing.image import ImageDataGenerator
from keras.optimizers import Adam
from keras.preprocessing.image import img_to_array
from keras.utils import to_categorical
from keras.utils import plot_model
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import numpy as np
import argparse as ag
import random,cv2,os,glob
from model_gender import gender_model


epochs = 10
lr = 1e-3
batch_size = 64
img_dims = (96,96,3)


data = []
labels = []

image_dir="/Users/chand/Documents/Projects/face_detection/dataset/"


image_files = [f for f in glob.glob(image_dir + "/**/*", recursive=True) if not os.path.isdir(f)] 

random.seed(42)
random.shuffle(image_files)



for img in image_files:
    
    image = cv2.imread(img)
    image = cv2.resize(image, (img_dims[0],img_dims[1]))
    image = img_to_array(image)
    data.append(image)
    
    
    label = img.split(os.path.sep)[-2]
    
    
    if label == 'woman':
        label = 1
        
    else:
        label =0
        
    labels.append([label])    



# pre-processing
data = np.array(data, dtype="float") / 255.0
labels = np.array(labels)



(X_train, X_test, Y_train, Y_test) = train_test_split(data, labels, test_size=0.2,
                                                  random_state=42)
Y_train = to_categorical(Y_train, num_classes=2)
Y_test = to_categorical(Y_test, num_classes=2)



img_data = ImageDataGenerator(rotation_range=25, width_shift_range=0.1,
                         height_shift_range=0.1, shear_range=0.2, zoom_range=0.2,
                         horizontal_flip=True, fill_mode="nearest")




model = gender_model.build(width=img_dims[0], height=img_dims[1], depth=img_dims[2],
                            classes=2)


opt = Adam(lr=lr, decay=lr/epochs)
model.compile(loss="binary_crossentropy", optimizer=opt, metrics=["accuracy"])




print("training started")

print("Length of training",len(X_train))

model.fit_generator(img_data.flow(X_train, Y_train, batch_size=batch_size),
                        validation_data=(X_test,Y_test),
                        steps_per_epoch=len(X_train) // batch_size,
                        epochs=epochs, verbose=1)





def save_model(model):

	model_json = model.to_json()

	with open("gender_classifier.json",'w') as json_file:
		json_file.write(model_json)


	model.save_weights("gender_classifier.h5")
	print("model_saved")



save_model(model)



