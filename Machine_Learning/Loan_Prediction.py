
# coding: utf-8

# In[39]:


import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


import seaborn as sns


# In[2]:


df=pd.read_csv('/Users/Chand/Downloads/LoanPrediction.csv')


# In[3]:


df.columns # to display the columns


# In[4]:


df.head()


# In[5]:


df.isnull().sum()


# In[6]:


df.dtypes   # to check the datatypes of the column


# In[7]:


def val_count(col):
    
    #col1 = df[col].unique()
    col= df[col].value_counts(dropna=False)
          
    return col
        


# In[8]:


cols=['Gender','Married','Dependents','Education','Self_Employed','Property_Area']


# In[9]:


for col in cols:
    print("\n")
    print("-------{} ------".format(col))
    print("\n")
    print("{}".format(val_count(col)))
    
    


# In[10]:


def null_check(col):
    col=df[col].isnull().sum()
    if col>0:
        return col
    
    else:
        pass
   
        


# In[11]:


for col in df.columns:
   
    print("{} ---- {}".format(col,null_check(col)))
   


# In[12]:


df['Credit_History'].fillna(0,inplace=True)    # Filling Na


# In[13]:


df['Gender'].value_counts()


# In[14]:



df['Married'].fillna(df['Married'].mode()[0], inplace=True)
df['Dependents'].fillna(df['Dependents'].mode()[0], inplace=True)
df['Self_Employed'].fillna(df['Self_Employed'].mode()[0], inplace=True)


# In[15]:


for col in df.columns:
   
    print("{} ---- {}".format(col,null_check(col)))


# In[16]:


df['LoanAmount'].fillna(df['LoanAmount'].mean(), inplace=True)


# In[17]:


df['Loan_Amount_Term'].fillna(df['Loan_Amount_Term'].mode()[0], inplace=True)


# In[18]:


for col in df.columns:
   
    print("{} ---- {}".format(col,null_check(col)))


# In[19]:


for col in cols:
    print("\n")
    print("-------{} ------".format(col))
    print("\n")
    print("{}".format(val_count(col)))


# In[20]:


df.dtypes


# In[21]:


df.dtypes


# In[22]:


for col in cols:
    print("\n")
    print("-------{} ------".format(col))
    print("\n")
    print("{}".format(val_count(col)))


# In[23]:


df['LoanAmount'].describe()


# In[24]:


sns.countplot(x='Gender',hue='Loan_Status',data=df)



# In[25]:


sns.countplot(x='Education',hue='Loan_Status',data=df)


# In[26]:


sns.barplot(x='Loan_Amount_Term',y='LoanAmount',hue='Loan_Status',data=df)


# In[27]:


sns.countplot(x='Property_Area',hue='Loan_Status',data=df)


# In[28]:


sns.countplot(x='Credit_History',hue='Loan_Status',data=df)


# In[29]:


sns.barplot(x='Credit_History',y='Loan_Amount_Term',hue='Loan_Status',data=df)




# In[30]:


sns.barplot(y='ApplicantIncome',x='Loan_Status',data=df)


# In[31]:


df['Loan_Status']= df['Loan_Status'].astype('category')
df['Loan_Status']= df['Loan_Status'].cat.codes


# In[32]:


sns.distplot(df['Loan_Status'])


# In[33]:


sns.countplot(x='Dependents',hue='Loan_Status',data=df)


# In[34]:


sns.distplot(df['LoanAmount'])


# In[35]:


sns.barplot(x='Property_Area',y='LoanAmount',hue='Loan_Status',data=df)


# In[36]:


for col_name in df.columns:
    if(df[col_name].dtype == 'object'):
        df[col_name]= df[col_name].astype('category')
        df[col_name] = df[col_name].cat.codes


# In[40]:


matrix = df.corr()
f, ax = plt.subplots(figsize=(12, 9))
sns.heatmap(matrix)


# In[44]:


x = df.drop(['Loan_Status','Loan_ID'],axis=1)
y = df.Loan_Status


# In[45]:


x


# In[46]:


y.value_counts()


# In[47]:


x['income']=x['ApplicantIncome']+x['CoapplicantIncome']


# In[50]:


x.drop(['ApplicantIncome','CoapplicantIncome'],axis=1,inplace=True)


# In[380]:


x=df.drop(['ApplicantIncome','CoapplicantIncome'],axis=1)


# In[51]:


x


# In[52]:


x.dtypes


# In[53]:


x


# In[54]:


x_train, x_test, y_train, y_test = train_test_split(x,y, test_size =0.3)


# In[55]:


x_train.shape, x_test.shape,y_train.shape,y_test.shape


# In[58]:


from sklearn.linear_model import LogisticRegression


# In[65]:


from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score


# In[60]:


log_reg = LogisticRegression()
log_reg.fit(x_train, y_train)


# In[92]:



y_pred=log_reg.predict(x_test)


# In[95]:


accuracy_score(y_test,y_pred)


# In[96]:


precision_score(y_test, y_pred, average='macro')  


# In[97]:


from sklearn.tree import DecisionTreeClassifier


# In[98]:



tree = DecisionTreeClassifier(random_state=0)


# In[99]:


tree.fit(x_train, y_train)


# In[100]:


y_pred=tree.predict(x_test)


# In[102]:


print("accuracy on training set: %f" % random_tree.score(x_train, y_train))
print("accuracy on test set: %f" % tree.score(x_test, y_test))


# In[103]:


from sklearn.ensemble import RandomForestClassifier


# In[104]:


random_tree= RandomForestClassifier()


# In[108]:


random_tree.fit(x_train, y_train)


# In[109]:


y_pred1=random_tree.predict(x_test)


# In[111]:


print("accuracy on training set: %f" % random_tree.score(x_train, y_train))
print("accuracy on test set: %f" % random_tree.score(x_test, y_test))

