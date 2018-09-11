
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[5]:


from sklearn.datasets import make_blobs
from sklearn.svm import LinearSVC


# In[6]:


svm = LinearSVC()


# We use a two-dimensional dataset, where each class is given by data sampled from a Gaussian distribution.

# In[3]:


X, y = make_blobs(random_state=42)


# In[4]:


plt.scatter(X[:, 0], X[:, 1], c=y, s=60)


# In[7]:


train=svm.fit(X,y)


# Here the classification is based one-vs-rest approach

# In[22]:


print(svm.coef_.shape)
print(svm.intercept_.shape)


# 
# 
# We see that the shape of the coef_ is (3, 2), meaning that each row of coef_ con‐ tains the coefficient vector for one of the three classes. Each row has two entries, cor‐ responding to the two features in the dataset.
# The intercept_ is now a one-dimensional array, storing the intercepts for each class.

# Let’s visualize the lines given by the three binary classifiers

# In[21]:


plt.scatter(X[:, 0], X[:, 1], c=y, s=60)
   
line = np.linspace(-10,15)


for coef, intercept in zip(svm.coef_, svm.intercept_):
   plt.plot(line, -(line * coef[0] + intercept) / coef[1])
   plt.ylim(-10, 15)
   plt.xlim(-10, 8)

