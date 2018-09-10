
# coding: utf-8

# In[26]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

get_ipython().run_line_magic('matplotlib', 'inline')


# In[4]:


iris= load_iris()  # loading the dataset


# The iris object that is returned by load_iris is a Bunch object, 
# which is very similar to a dictionary. It contains keys and values

# In[6]:


iris.keys()


# In[11]:


print(iris['DESCR'] + "\n...")


# In[12]:


iris['target_names']


# In[13]:


iris['feature_names']


# In[15]:


# array: 0 means Setosa, 1 means Versicolor and 2 means Virginica.


# In[14]:


iris['target']


# In[17]:


X_train, X_test, y_train, y_test = train_test_split(iris['data'], iris['target'],random_state=0)
                                                        


# In[20]:


X_train.shape  # split was made as 75% training and 25% as test data


# In[21]:


X_test.shape


# In[27]:


fig, ax = plt.subplots(3, 3, figsize=(15, 15))
plt.suptitle("iris_pairplot")

for i in range(3):
    for j in range(3):
        ax[i, j].scatter(X_train[:, j], X_train[:, i + 1], c=y_train, s=60)
        ax[i, j].set_xticks(())
        ax[i, j].set_yticks(())
        if i == 2:
            ax[i, j].set_xlabel(iris['feature_names'][j])
        if j == 0:
            ax[i, j].set_ylabel(iris['feature_names'][i + 1])
        if j > i:
            ax[i, j].set_visible(False)


# In[28]:


from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=1)


# n_neighbors : int, optional (default = 5)
# 
# 
# weights : str or callable, optional (default = ‘uniform’)
# 
# weight function used in prediction. Possible values:
# 
# ‘uniform’ : uniform weights. All points in each neighborhood are weighted equally.
# 
# ‘distance’ : weight points by the inverse of their distance.
# 
# in this case, closer neighbors of a query point will have a greater influence than neighbors which are further away.
# 
# [callable] : a user-defined function which accepts an array of distances, and returns an array of the same shape containing the weights.

# algorithm : {‘auto’, ‘ball_tree’, ‘kd_tree’, ‘brute’}, optional
# Algorithm used to compute the nearest neighbors:
# ‘ball_tree’ will use BallTree
# ‘kd_tree’ will use KDTree
# ‘brute’ will use a brute-force search.
# ‘auto’ will attempt to decide the most appropriate algorithm based on the values passed to fit method.

# n_jobs : int, optional (default = 1)
# The number of parallel jobs to run for neighbors search. If -1, then the number of jobs is set to the number of CPU cores. Doesn’t affect fit method.

# knn.fit(X_train, y_train)
# KNeighborsClassifier(algorithm='auto', leaf_size=30, metric='minkowski',
#                metric_params=None, n_jobs=1, n_neighbors=1, p=2,
#                weights='uniform')

# In[30]:


y_pred = knn.predict(X_test)
np.mean(y_pred == y_test)


# In[31]:


knn.score(X_test, y_test)

