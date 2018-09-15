
# coding: utf-8

# In[49]:


from sklearn.tree import DecisionTreeClassifier
from sklearn import datasets
from sklearn.model_selection import train_test_split
import pandas as pd


# In[7]:


cancer = datasets.load_breast_cancer()


# In[48]:


cancer.keys()


# In[40]:


cancer['feature_names']


# In[53]:


cancer['data']


# In[8]:


X_train, X_test, y_train, y_test = train_test_split(
        cancer.data, cancer.target, stratify=cancer.target, random_state=42)


# In[9]:


tree = DecisionTreeClassifier(random_state=0)


# In[10]:


tree.fit(X_train, y_train)


# In[12]:


print("accuracy on training set: %f" % tree.score(X_train, y_train))
print("accuracy on test set: %f" % tree.score(X_test, y_test))


# In[ ]:


# Overfitting


# In[13]:


# Pruning  reducing the depth to control overfitting


# In[28]:


tree = DecisionTreeClassifier(max_depth=3, random_state=0)
tree.fit(X_train, y_train)


# In[29]:


print("accuracy on training set: %f" % tree.score(X_train, y_train))
print("accuracy on test set: %f" % tree.score(X_test, y_test))


# In[44]:


# Because of pruning got better result on test data


# In[30]:


from sklearn.tree import export_graphviz


# In[31]:


# Exporting the graphviz


# In[32]:


export_graphviz(tree, out_file="mytree.dot", class_names=["malignant", "benign"],
                    feature_names=cancer.feature_names, impurity=False, filled=True)


# In[33]:


# Importing the graphviz


# In[34]:


import graphviz

with open("mytree.dot") as f:
    dot_graph = f.read()
    


# In[35]:


graphviz.Source(dot_graph)

