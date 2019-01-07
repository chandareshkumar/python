
# coding: utf-8

# In[1]:


import numpy as np
import keras.models
from keras.models import model_from_json
from scipy.misc import imread, imresize,imshow


# In[2]:


json_file = open('/Users/chand/model.json','r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
#load woeights into new model
loaded_model.load_weights("/Users/chand/model.h5")
loaded_model.compile(loss='categorical_crossentropy',optimizer='adam',metrics=['accuracy'])
print("Loaded Model from disk")


# In[3]:


#loaded_model.compile(loss='categorical_crossentropy',optimizer='adam',metrics=['accuracy'])


# In[79]:


x = imread('/Users/chand/Documents/Python/output.png',mode='L')


# In[80]:




x = np.invert(x)


# In[82]:




# In[83]:


x = imresize(x,(28,28))


# In[84]:


x.shape


# In[85]:


import matplotlib.pyplot as plt
plt.imshow(np.uint8(x))
plt.show()


# In[86]:


x = x.reshape(1,28,28,1)


# In[87]:
def prediction(y):

	out = loaded_model._make_predict_function(y)
	print(out)
	print(np.argmax(out,axis=1))
	return out

