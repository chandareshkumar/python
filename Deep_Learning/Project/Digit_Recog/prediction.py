import tensorflow as tf
from keras.models import load_model
import cv2
import numpy as np
from scipy import ndimage
import math

classes=[0,1,2,3,4,5,6,7,8,9]

model=tf.keras.models.load_model('digit_recog_cnn.h5')
def testing1():
    img=cv2.imread('image.png',0)
    img=cv2.bitwise_not(img)

    img=cv2.resize(img,(28,28))
    cv2.imshow('img',img)
    img=img.reshape(1,28,28,1)

    img=img.astype('float32')

    img=img/255.0


    pred=model.predict(img)
    return pred

def testing():
    gray=cv2.imread('image.png',cv2.IMREAD_GRAYSCALE)
    gray = cv2.resize(255-gray, (28, 28))
    (thresh, gray) = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

    while np.sum(gray[0]) == 0:
        gray = gray[1:]

    while np.sum(gray[:,0]) == 0:
        gray = np.delete(gray,0,1)

    while np.sum(gray[-1]) == 0:
        gray = gray[:-1]

    while np.sum(gray[:,-1]) == 0:
        gray = np.delete(gray,-1,1)

    rows,cols = gray.shape

    if rows > cols:
        factor = 20.0/rows
        rows = 20
        cols = int(round(cols*factor))
        gray = cv2.resize(gray, (cols,rows))
    else:
        factor = 20.0/cols
        cols = 20
        rows = int(round(rows*factor))
        gray = cv2.resize(gray, (cols, rows))


    colsPadding = (int(math.ceil((28-cols)/2.0)),int(math.floor((28-cols)/2.0)))
    rowsPadding = (int(math.ceil((28-rows)/2.0)),int(math.floor((28-rows)/2.0)))

    shiftx,shifty = getBestShift(gray)
    shifted = shift(gray,shiftx,shifty)
    gray = shifted

    img = np.lib.pad(gray,(rowsPadding,colsPadding),'constant')
   # cv2.imshow('img',img)
    img=img.reshape(1,28,28,1)

    pred=model.predict(img)
    return pred

def getBestShift(img):
    cy,cx = ndimage.measurements.center_of_mass(img)

    rows,cols = img.shape
    shiftx = np.round(cols/2.0-cx).astype(int)
    shifty = np.round(rows/2.0-cy).astype(int)

    return shiftx,shifty

def shift(img,sx,sy):
    rows,cols = img.shape
    M = np.float32([[1,0,sx],[0,1,sy]])
    shifted = cv2.warpAffine(img,M,(cols,rows))
    return shifted


