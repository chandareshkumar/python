
# coding: utf-8

# In[1]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


df1=pd.read_excel("/Users/chand/Downloads/DA-1.xlsx",sheet_name=1) # importing data sheet1


# In[3]:


df1.shape


# In[4]:


df2=pd.read_excel("/Users/chand/Downloads/DA-1.xlsx")  # importing data sheet2


# In[5]:


df1.columns


# In[6]:


df2.columns


# In[7]:


df2[df2.isnull().values]   #checking the null values


# In[8]:


df2['Type'].fillna(df2['Type'].mode()[0], inplace=True)  #imputing the null values with mode


# In[9]:


df2[df2.isnull().values]


# In[10]:


df2.dropna(axis='rows',inplace=True)  #dropping the null values


# In[11]:


df2[df2.isnull().values]


# In[12]:


df2.FeedBack.value_counts()


# In[13]:


# duplicate categories is found because of lower and upper case mix.

# to group them lets convert all characters to UPPER CASE


# In[14]:


df2['FeedBack']=df2['FeedBack'].astype(str).apply( lambda x : x.upper().strip())  #strip added to remove white space


# In[15]:


df2.FeedBack.value_counts()  # clubbed categories together


# In[16]:


sns.distplot(df2['CountA'])  # checking the distribution of values in countA


# In[17]:


sns.distplot(df2['CountB'])  # checking the distribution of values in countB


# In[18]:


sns.distplot(df2['CountC'])    # checking the distribution of values in countC


# In[19]:


df1["is_duplicate"]= df1['Id'].duplicated()  # checking for the duplicate values


# In[20]:


df1[df1['is_duplicate']==True]


# In[21]:


df1[df1['Id']==10127]


# In[22]:


df1.drop_duplicates('Id', keep='first', inplace=True)  #dropping the duplicate values


# In[23]:


df1


# In[24]:


df1.drop('is_duplicate',axis=1,inplace=True)


# In[31]:


df3=df1.join(df2.set_index('Id'),on='Id',how='right')  # joing two sheet based on key - Id (Right join)


# In[32]:


df3


# In[33]:



summary=pd.crosstab(df3.Type, df3.User)


# In[34]:


summary     #summary of the users


# In[35]:


summary.plot.bar()


# In[36]:


pd.crosstab(df3.Type, df3.User,margins=True)


# In[37]:


def time_split(data):
    
    df3['Year']=df3[data].dt.year
    df3['Month']=df3[data].dt.month
    df3['Day']= df3[data].dt.day
    df3['Hour'] = df3[data].dt.hour
    df3['Minutes']=df3[data].dt.minute


# In[38]:


time_split('Date')


# In[39]:


print("Year",df3['Year'].unique())
print("Month",df3['Month'].unique())        #splitting time series
print("Day",df3['Day'].unique())
print("Hour",df3['Hour'].unique())
print("Minutes",df3['Minutes'].unique())


# In[40]:


df3.drop(['Date','Month','Year','Day'], axis=1, inplace=True)  #dropping Month, Year, Day as all values were same


# In[41]:


sns.countplot(x='Type',data=df3)   #checking the frequency of Type


# In[42]:


sns.countplot(x='FeedBack',data=df3)


# In[43]:


sns.countplot(x='User',data=df3)


# In[44]:


df3['CountA'].describe()


# In[45]:


df3['CountB'].describe()


# In[46]:


df3['CountC'].describe()


# In[97]:


plt.figure(figsize=(15,7))
plt.scatter(x=df3['CountA'], y=df3['FeedBack'])
plt.xlabel('A Count')
plt.ylabel('FeedBack')


# In[48]:


plt.figure(figsize=(15,7))
plt.scatter(x=df3['CountB'], y=df3['FeedBack'])
plt.xlabel('B Count')
plt.ylabel('FeedBack')


# In[49]:


plt.figure(figsize=(15,7))
plt.scatter(x=df3['CountC'], y=df3['FeedBack'])
plt.xlabel('C Count')
plt.ylabel('FeedBack')


# In[50]:


plt.figure(figsize=(15,7))
plt.scatter(x=df3['Hour'], y=df3['FeedBack'])
plt.xlabel('Hour')
plt.ylabel('FeedBack')


# In[51]:


plt.figure(figsize=(15,7))
plt.scatter(x=df3['Minutes'], y=df3['FeedBack'])
plt.xlabel('Minutes')
plt.ylabel('FeedBack')


# In[52]:


plt.figure(figsize=(15,7))
plt.scatter(x=df3['Type'], y=df3['FeedBack'])
plt.xlabel('Hour')
plt.ylabel('FeedBack')


# In[53]:


# email has high coorelation to others


# In[54]:


sns.boxplot(df3['Minutes'])


# In[55]:


sns.boxplot(df3['Hour'])


# In[56]:


df3.Hour.describe()


# In[57]:


df3[df3['Hour']<13] # here we have more values within the range, hence those points are not outliers


# In[58]:


sns.barplot(x='Minutes',y='FeedBack',data=df3)


# In[96]:


plt.figure(figsize=(15,7))
plt.hist(df3['Hour'], bins=15)
plt.xlabel('Hour')
plt.ylabel('Frequency')


# In[60]:


plt.figure(figsize=(15,7))
plt.hist(df3['Minutes'], bins=200)
plt.xlabel('Minutes')
plt.ylabel('Frequency')


# In[61]:


df3['Total']=df3['CountA'] + df3['CountB'] + df3['CountC']


# In[62]:


sns.distplot(df3['Total'])


# In[63]:


plt.figure(figsize=(15,7))
plt.scatter(x=df3['Total'], y=df3['FeedBack'])
plt.xlabel('Total')
plt.ylabel('FeedBack')


# In[66]:


df3.Total.describe()


# In[65]:


matrix = df3.corr()
f, ax = plt.subplots(figsize=(12, 9))    # correlation matrix
sns.heatmap(matrix)


# In[67]:


def codes(data):
    
    df3[data] = df3[data].astype('category')   #converting the object type to numerical values
    df3[data] = df3[data].cat.codes


# In[68]:


codes('Type')


# In[69]:


codes('FeedBack')


# In[70]:


codes('User')


# In[71]:


df3['FeedBack'].unique()


# In[72]:


plt.figure(figsize=(15,7))
plt.scatter(x=df3['User'], y=df3['FeedBack'])
plt.xlabel('User')
plt.ylabel('FeedBack')


# In[73]:


df3.dtypes


# In[74]:


df3.drop('Id',axis=1,inplace=True)  


# In[75]:


df3.drop('User',axis=1,inplace=True) # to generalise for all user -- dropping the column


# In[76]:


x = df3.iloc[:,df3.columns!='FeedBack']   #preparing x, y values
y = df3['FeedBack'].values


# In[77]:


from sklearn.model_selection import train_test_split


# In[78]:


x_train, x_test, y_train, y_test = train_test_split(x,y, test_size =0.2)   #splitting training and test data


# In[79]:


x_train.shape


# In[80]:


x_test.shape


# In[81]:


y_train.shape


# In[82]:


from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score




# In[83]:


log_reg = LogisticRegression()
log_reg.fit(x_train, y_train)



# In[84]:


y_pred=log_reg.predict(x_test)


# In[85]:


accuracy_score(y_test,y_pred)  # prediction score


# In[86]:


df3['FeedBack'].unique()


# In[87]:


from sklearn.ensemble import RandomForestClassifier
RF = RandomForestClassifier()
RF.fit(x_train, y_train)
y_pred = RF.predict(x_test)


# In[88]:


y_pred


# In[89]:


accuracy_score(y_test,y_pred)  # prediction score


# In[90]:


from sklearn.naive_bayes import GaussianNB    #Naive Bayes treats every column as independent feature


# In[91]:


gnb = GaussianNB()


# In[92]:


gnb.fit(x_train, y_train) 


# In[93]:


y_pred=gnb.predict(x_test)


# In[94]:


accuracy_score(y_test,y_pred) 


# In[95]:


# so based on accuracy score we can build our model using RandomForestClassifier

