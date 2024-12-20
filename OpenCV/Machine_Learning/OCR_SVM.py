
# coding: utf-8

# In[3]:


import cv2
import numpy as np

SZ=20
bin_n = 16 # Number of bins

svm_params = dict( kernel_type = cv2.ml.SVM_LINEAR,
                    svm_type = cv2.ml.SVM_C_SVC,
                    C=2.67, gamma=5.383 )

affine_flags = cv2.WARP_INVERSE_MAP|cv2.INTER_LINEAR


# In[4]:


def deskew(img):
    m = cv2.moments(img)
    if abs(m['mu02']) < 1e-2:
        return img.copy()
    skew = m['mu11']/m['mu02']
    M = np.float32([[1, skew, -0.5*SZ*skew], [0, 1, 0]]) 
    img = cv2.warpAffine(img,M,(SZ, SZ),flags=affine_flags) 
    return img


# In[6]:


def hog(img):
    gx = cv2.Sobel(img, cv2.CV_32F, 1, 0) 
    gy = cv2.Sobel(img, cv2.CV_32F, 0, 1) 
    mag, ang = cv2.cartToPolar(gx, gy)
    # quantizing binvalues in (0...16)
    bins = np.int32(bin_n*ang/(2*np.pi))
    # Divide to 4 sub-squares
    bin_cells = bins[:10,:10], bins[10:,:10], bins[:10,10:], bins[10:,10:]
    mag_cells = mag[:10,:10], mag[10:,:10], mag[:10,10:], mag[10:,10:]
    hists = [np.bincount(b.ravel(), m.ravel(), bin_n) for b, m in zip(bin_cells, mag_cells)]
    hist = np.hstack(hists) 
    return hist


# In[46]:


img = cv2.imread('/Users/chand/Downloads/digits.png',0)

cells = [np.hsplit(row,100) for row in np.vsplit(img,50)]
# First half is trainData, remaining is testData
train_cells = [ i[:50] for i in cells ] 

test_cells = [ i[50:] for i in cells]

######     Now training      ########################

deskewed = [map(deskew,row) for row in train_cells]
hogdata = [list(map(hog,row)) for row in deskewed]
trainData = np.float32((hogdata)).reshape(-1,64)


#responses = np.float32(np.repeat(np.arange(10),250)[:,np.newaxis])
responses = np.int32(np.repeat(np.arange(10),250)[:,np.newaxis])



svm = cv2.ml.SVM_create()
svm.setKernel(cv2.ml.SVM_LINEAR)
svm.setType(cv2.ml.SVM_C_SVC)
svm.setC(2.67)
svm.setGamma(5.383)
svm.train(trainData, cv2.ml.ROW_SAMPLE, responses)
svm.save('svm_data.dat')

deskewed = [list(map(deskew,row)) for row in test_cells]
hogdata = [list(map(hog,row)) for row in deskewed]
testData = np.float32(hogdata).reshape(-1,bin_n*4)
result = svm.predict(testData)[1]
mask = result==responses
correct = np.count_nonzero(mask)
print(correct*100.0/result.size)

