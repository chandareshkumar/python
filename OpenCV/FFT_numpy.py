
# coding: utf-8

# In[16]:


import cv2
import numpy as np
from matplotlib import pyplot as plt


# The Fourier Transform is an important image processing tool which is used to 
# decompose an image into its sine and cosine components. 
# The output of the transformation represents the image in the Fourier or frequency domain, 
# while the input image is the spatial domain equivalent.

# In[17]:


img = cv2.imread('/Users/chand/Downloads/fox.jpg',0)
f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)
magnitude_spectrum = 20*np.log(np.abs(fshift))


# np.fft.fft2() provides us the frequency transform which will be a complex array. 
# Its first argument is the input image, which is grayscale. Second argument is optional which decides the size of output array. 
# If it is greater than size of input image, input image is padded with zeros before calculation of FFT. 
# If it is less than input image, input image will be cropped. 
# If no arguments passed, Output array size will be same as input.
Now once you got the result, zero frequency component (DC component) will be at top left corner. 
If you want to bring it to center, you need to shift the result by \frac{N}{2} in both the directions. 
This is simply done by the function, np.fft.fftshift(). (It is more easier to analyze). 
Once you found the frequency transform, you can find the magnitude spectrum.
# In[18]:


plt.subplot(121),plt.imshow(img, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(magnitude_spectrum, cmap = 'gray')
plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
plt.show()


# In[20]:


rows, cols = img.shape
crow,ccol = int(rows/2) , int(cols/2)

fshift[crow-30:crow+30, ccol-30:ccol+30] = 0
f_ishift = np.fft.ifftshift(fshift)
img_back = np.fft.ifft2(f_ishift)
img_back = np.abs(img_back)



# So you found the frequency transform Now you can do some operations in frequency domain, like high pass filtering and reconstruct the image, ie find inverse DFT. For that you simply remove the low frequencies by masking with a rectangular window of size 60x60. Then apply the inverse shift using np.fft.ifftshift() so that DC component again come at the top-left corner. Then find inverse FFT using np.ifft2() function. The result, again, will be a complex number. You can take its absolute value.

# In[21]:


plt.subplot(131),plt.imshow(img, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(132),plt.imshow(img_back, cmap = 'gray')
plt.title('Image after HPF'), plt.xticks([]), plt.yticks([])
plt.subplot(133),plt.imshow(img_back)
plt.title('Result in JET'), plt.xticks([]), plt.yticks([])

plt.show()

