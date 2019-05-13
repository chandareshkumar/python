

import keras




from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPooling2D
from keras import backend as k


batch_size =128



num_classes=10



epochs=12




img_rows, img_cols = 28,28




(x_train, y_train), (x_test, y_test) = mnist.load_data()





if k.image_data_format=='channels_first':   #NCHW
    x_train=x_train.reshape(x_train.shape[0],1,img_rows,img_cols)
    x_test=x_test.reshape(x_test.shape[0],1,img_rows,img_cols)
    input_shape=(1,img_rows,img_cols)

else:
    x_train=x_train.reshape(x_train.shape[0],img_rows,img_cols,1)
    x_test=x_test.reshape(x_test.shape[0],img_rows,img_cols,1)
    input_shape=(img_rows,img_cols,1)




#more reshaping
x_train = x_train.astype('float32')
x_test = x_test.astype('float32')



x_train /= 255
x_test /= 255



print('x_train shape:', x_train.shape)
print(x_train.shape[0], 'train samples')
print(x_test.shape[0], 'test samples')




# convert class vectors to binary class matrices
y_train = keras.utils.to_categorical(y_train, num_classes)
y_test = keras.utils.to_categorical(y_test, num_classes)




#build our model
model = Sequential()
#convolutional layer with rectified linear unit activation
model.add(Conv2D(32, kernel_size=(3, 3),
                 activation='relu',
                 input_shape=input_shape))
#again
model.add(Conv2D(64, (3, 3), activation='relu'))
#choose the best features via pooling
model.add(MaxPooling2D(pool_size=(2, 2)))
#randomly turn neurons on and off to improve convergence
model.add(Dropout(0.25))
#flatten since too many dimensions, we only want a classification output
model.add(Flatten())
#fully connected to get all relevant data
model.add(Dense(128, activation='relu'))
#one more dropout for convergence' sake :) 
model.add(Dropout(0.5))
#output a softmax to squash the matrix into output probabilities
model.add(Dense(num_classes, activation='softmax'))



#Adaptive learning rate (adaDelta) is a popular form of gradient descent rivaled only by adam and adagrad
#categorical ce since we have multiple classes (10) 
model.compile(loss=keras.losses.categorical_crossentropy,
              optimizer=keras.optimizers.Adadelta(),
              metrics=['accuracy'])




model.fit(x_train, y_train,
          batch_size=batch_size,
          epochs=epochs,
          verbose=1,
          validation_data=(x_test, y_test))





score = model.evaluate(x_test, y_test, verbose=0)
print('Test loss:', score[0])
print('Test accuracy:', score[1])


# In[1]:


from keras.datasets import mnist 
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

from keras import models
from keras import layers

#create a sequential model
network = models.Sequential()
# layer one with 512 nodes (arbitrary) and relu as activation function, input_shape is the input dimension expected by the layer
# here, it is 28 by 28 pixel, flattened to 784 x 1 vector
network.add(layers.Dense(512, activation='relu',input_shape=(28*28,)))
#output layer 
network.add(layers.Dense(10, activation='softmax'))

#compile the network by providing the optimizer, loss function and the metrics to monitor
network.compile(optimizer='rmsprop', loss='categorical_crossentropy', metrics=['accuracy'])

#flatten out the input data into a 784x1 vector, convert pixel values from uint8 to float32, and range from 
# 0 255 to the interval [0,1]
train_images = train_images.reshape((60000,28*28))
train_images = train_images.astype('float32') / 255

test_images = test_images.reshape((10000,28*28))
test_images = test_images.astype('float32') / 255

#convert the labels to one hot vector form
#Example , if there are 3 classes 1,2 and 3, the one hot vector representation would be like
# class 1 => [1, 0, 0]
# class 2 => [0, 1, 0]
# class 3 => [0, 0, 1]
from keras.utils import to_categorical
train_labels = to_categorical(train_labels)
test_labels = to_categorical(test_labels)

#epochs is the number of iterations over the entire dataset
network.fit(train_images, train_labels, epochs=5, batch_size=128)

# Evaluate the model on the test data.
test_loss, test_acc = network.evaluate(test_images, test_labels)

print('test accuracy: ', test_acc)


# In[26]:


#Save the model
# serialize model to JSON
model_json = model.to_json()
with open("model.json", "w") as json_file:
    json_file.write(model_json)
# serialize weights to HDF5
model.save_weights("model.h5")
print("Saved model to disk")

