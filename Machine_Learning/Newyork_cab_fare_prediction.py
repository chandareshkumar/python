
# coding: utf-8

# In[4]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns


# In[30]:


train=pd.read_csv("/Users/chand/Downloads/all/train.csv",nrows=1000000)


# In[31]:


test=pd.read_csv("/Users/chand/Downloads/all/test.csv")


# In[32]:


train.shape


# In[33]:


test.shape


# In[34]:


test.columns


# In[35]:


train.columns


# In[36]:


train.dtypes


# In[37]:


train.describe()


# In[38]:


train.isnull().sum().sort_values(ascending=True)


# In[39]:


test.isnull().sum().sort_values(ascending=False)


# In[40]:




train.dropna(inplace=True,axis='rows')


# In[41]:


train.shape


# In[42]:


train.isnull().sum().sort_values(ascending=False)


# In[47]:


train['fare_amount'].describe()


# In[59]:


train['fare_amount'][train['fare_amount']<0].count()


# In[83]:


train.drop(train[train['fare_amount']<0].index,axis='rows',inplace=True) # fare can't be negative hence removing them


# In[84]:


train.shape


# In[85]:


train.fare_amount.describe()


# In[86]:


fare=train.fare_amount.sort_values(ascending=False)


# In[87]:


count=0
for i in fare:
    if i ==0:
        count=count + 1
print(count)        


# In[81]:


sns.distplot(train['fare_amount'])


# In[88]:


train['passenger_count'].describe()


# In[92]:


sns.boxplot(train['passenger_count'])  # to check outlier


# In[95]:




train.drop(train[train['passenger_count']>10].index,axis='rows',inplace=True) 


# In[98]:


train['passenger_count'].describe()


# In[99]:


train['pickup_latitude'].describe()


# 
# Latitudes range from -90 to 90.
# Longitudes range from -180 to 180.
# 

# In[105]:


sns.boxplot(train['pickup_latitude'])


# In[118]:


train.drop(train[(train['pickup_latitude']<-90 )| (train['pickup_latitude']>90.0)].index, axis=0,inplace=True)


# In[121]:


sns.distplot(train['pickup_latitude'])


# In[124]:


train['dropoff_latitude'].describe()


# In[125]:


train.drop(train[(train['dropoff_latitude']<-90 )| (train['dropoff_latitude']>90.0)].index, axis=0,inplace=True)


# In[126]:


train['dropoff_latitude'].describe()


# In[128]:


train.drop(train[(train['pickup_longitude']<-180 )| (train['pickup_longitude']>180.0)].index, axis=0,inplace=True)
train.drop(train[(train['dropoff_longitude']<-180 )| (train['dropoff_longitude']>180.0)].index, axis=0,inplace=True)


# In[129]:


train['dropoff_longitude'].describe()


# In[130]:


train.dtypes



# In[133]:


train[['key','pickup_datetime']]


# In[134]:


train['key'] = pd.to_datetime(train['key'])
train['pickup_datetime']  = pd.to_datetime(train['pickup_datetime'])


# In[135]:


test['key'] = pd.to_datetime(test['key'])
test['pickup_datetime']  = pd.to_datetime(test['pickup_datetime'])


# In[138]:


train.dtypes


# In[139]:


# Distance between lat and long can be calculated using Haversine distance 


# In[140]:


def haversine_distance(lat1, long1, lat2, long2):
    data = [train, test]
    for i in data:
        R = 6371  #radius of earth in kilometers
        #R = 3959 #radius of earth in miles
        
        phi1 = np.radians(i[lat1])
        phi2 = np.radians(i[lat2])
    
        delta_phi = np.radians(i[lat2]-i[lat1])
        delta_lambda = np.radians(i[long2]-i[long1])
    
        #a = sin²((φB - φA)/2) + cos φA . cos φB . sin²((λB - λA)/2)
        
        a = np.sin(delta_phi / 2.0) ** 2 + np.cos(phi1) * np.cos(phi2) * np.sin(delta_lambda / 2.0) ** 2
    
        #c = 2 * atan2( √a, √(1−a) )
        
        c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1-a))
    
        #d = R*c
        
        d = (R * c) #in kilometers
        
        i['H_Distance'] = d
        
    return d


# In[141]:


haversine_distance('pickup_latitude', 'pickup_longitude', 'dropoff_latitude', 'dropoff_longitude')


# In[144]:


test['H_Distance'].count()


# In[146]:


def time_split(data):
    
    train['Year']=train[data].dt.year
    train['Month']=train[data].dt.month
    train['Date']=train[data].dt.day
    train['Day_of_week']=train[data].dt.dayofweek
    train['hour'] = train[data].dt.hour
    
    test['Year']=test[data].dt.year
    test['Month']=test[data].dt.month
    test['Date']=test[data].dt.day
    test['Day_of_week']=test[data].dt.dayofweek
    test['hour'] = test[data].dt.hour
    


# In[148]:


time_split('pickup_datetime')


# In[149]:


train.head()


# In[150]:


plt.figure(figsize=(15,7))
plt.hist(train['passenger_count'], bins=15)
plt.xlabel('No. of Passengers')
plt.ylabel('Frequency')


# In[158]:



plt.scatter(train['passenger_count'],train['fare_amount'])


# In[159]:


plt.figure(figsize=(15,7))
plt.scatter(x=train['Date'], y=train['fare_amount'])
plt.xlabel('Date')
plt.ylabel('Fare')


# In[162]:


plt.figure(figsize=(15,7))
plt.hist(train['hour'], bins=100)
plt.xlabel('Hour')
plt.ylabel('Frequency')



# In[164]:


plt.figure(figsize=(15,7))
plt.scatter(x=train['hour'], y=train['fare_amount'])
plt.xlabel('Hour')
plt.ylabel('Fare')


# In[169]:


plt.figure(figsize=(15,7))
plt.hist(train['Day_of_week'],bins=20)
plt.xlabel('Day of Week')
plt.ylabel('Frequency')


# In[171]:


plt.figure(figsize=(15,7))
plt.scatter(x=train['Day_of_week'], y=train['fare_amount'])
plt.xlabel('Day of Week')
plt.ylabel('Fare')


# In[190]:


train['H_Distance'][train['H_Distance']>100].count()


# There are values which are greater than 100 kms! In NYC I am not sure why people would take cabs to travel more than a 100 kms. Since the number of bins for 100-200 kms is quite high, I will keep these. These outliers could be because of typos or missing values in the latitude or longitude. Remove fields of the following -
# 
# Pickup latitude and pickup longitude are 0 but dropoff latitude and longitude are not 0, but the fare is 0
# vice versa of point 1.
# Pickup latitude and pickup longitude are 0 but dropoff latitude and longitude are not 0, but the fare is NOT 0. Here I will have to impute the distance values in both the train and test data.
# 

# In[191]:


#pickup latitude and longitude = 0
train.loc[((train['pickup_latitude']==0) & (train['pickup_longitude']==0))&((train['dropoff_latitude']!=0) & (train['dropoff_longitude']!=0)) & (train['fare_amount']==0)]


# In[192]:


train = train.drop(train.loc[((train['pickup_latitude']==0) & (train['pickup_longitude']==0))&((train['dropoff_latitude']!=0) & (train['dropoff_longitude']!=0)) & (train['fare_amount']==0)].index, axis=0)


# In[193]:


train.shape


# In[ ]:


dist_bins =pd.concat([bins_0,bins_1,bins_2,bins_3,bins_4,bins_5,bins_6])

dist_bins.columns


# In[194]:


test.loc[((test['pickup_latitude']==0) & (test['pickup_longitude']==0))&((test['dropoff_latitude']!=0) & (test['dropoff_longitude']!=0))]


# In[195]:


train.loc[((train['pickup_latitude']!=0) & (train['pickup_longitude']!=0))&((train['dropoff_latitude']==0) & (train['dropoff_longitude']==0)) & (train['fare_amount']==0)]


# In[196]:


train = train.drop(train.loc[((train['pickup_latitude']!=0) & (train['pickup_longitude']!=0))&((train['dropoff_latitude']==0) & (train['dropoff_longitude']==0)) & (train['fare_amount']==0)].index, axis=0)


# In[197]:


test.loc[((test['pickup_latitude']!=0) & (test['pickup_longitude']!=0))&((test['dropoff_latitude']==0) & (test['dropoff_longitude']==0))]


# In[198]:


high_distance = train.loc[(train['H_Distance']>200)&(train['fare_amount']!=0)]


# In[206]:


train[['H_Distance','fare_amount']].sort_values(['H_Distance','fare_amount'],ascending=False)


# In[207]:


plt.figure(figsize=(15,7))
plt.scatter(x=train['H_Distance'], y=train['fare_amount'])
plt.xlabel('Distance')
plt.ylabel('Fare')


# In[210]:


train[train['H_Distance']==0].H_Distance.count()


# 
# 
# 
# We can see a few rows with distance =0. This could be due to 2 reasons
# 
# The cab waited the whole time and the passenger eventually cancelled. That's why the pickup and drop co-ordinates are the same and maybe, the passenger was charged for the waiting time.
# The pickup and drop co-ordinates were not entered. In other words, these are missing values!

# In[211]:


train[(train['H_Distance']==0)&(train['fare_amount']==0)]


# In[212]:


train = train.drop(train[(train['H_Distance']==0)&(train['fare_amount']==0)].index, axis = 0)


# In[213]:


train[(train['H_Distance']==0)].shape


# DataFrame.loc  --> .loc(a,b))
# 
# a --> condition(result boolean)
# 
# b --> columns(optional)
# 
# loc returns only true value index and corresponding columns

# 
# missing distance values with the fare and average price per kilometer of NYC cabs.
# 
# A quick Google search gave me the following prices -
# 
# $$2.5 base-price + $1.56/km --> 6AM to 8PM Mon-Fri
# 
# $$3.0 base-price + $1.56/km --> 8PM to 6AM Mon-Fri and Sat&Sun

# In[225]:


high_distance['H_Distance'] = high_distance.apply(
    lambda row: (row['fare_amount'] - 2.50)/1.56,
    axis=1
)


# In[223]:


train.update(high_distance)


# In[226]:





# In[217]:


rush_hour = train.loc[(((train['hour']>=6)&(train['hour']<=20)) & ((train['Day_of_week']>=1) & 
                                                                   (train['Day_of_week']<=5)) & 
                       (train['H_Distance']==0) & (train['fare_amount'] < 2.5))]


# In[218]:


rush_hour


# In[227]:


#Between 8PM and 6AM on Mon-Fri
non_rush_hour = train.loc[(((train['hour']<6)|(train['hour']>20)) & ((train['Day_of_week']>=1)&(train['Day_of_week']<=5)) & (train['H_Distance']==0) & (train['fare_amount'] < 3.0))]

non_rush_hour
#keep these. Since the fare_amount is not <2.5 (which is the base fare), these values seem legit to me.


# In[234]:


#Saturday and Sunday all hours
weekends = train.loc[((train['Day_of_week']==0) | (train['Day_of_week']==6)) & (train['H_Distance']==0) & (train['fare_amount'] < 3.0)]
weekends

#keep these too. Since the fare_amount is not <2.5, these values seem legit to me.


# In[242]:


train[(train['fare_amount']==0) & (train['H_Distance'] !=0)]


# Fare is 0, but Distance is not 0. These values need to be imputed.
# 
# I can calculate the fare as I have the distance. I shall use the following formula
# 
# fare = 2.5 + 1.56(H_Distance)

# In[243]:


amount= train.loc[(train['H_Distance']!=0) & (train['fare_amount']==0)]


# In[244]:


amount['fare_amount'] = amount.apply(
    lambda row: ((row['H_Distance'] * 1.56) + 2.50), axis=1
)


# In[246]:


train.loc[(train['H_Distance']!=0) & (train['fare_amount']==0)]


# In[247]:


train.update(amount)


# In[248]:


train.loc[(train['H_Distance']!=0) & (train['fare_amount']==0)]


# Fare is not 0, but Distance is 0. These values need to be imputed.

# In[249]:


train.loc[(train['H_Distance']==0) & (train['fare_amount']!=0)]


# In[251]:


dist_fare =train.loc[(train['H_Distance']==0) & (train['fare_amount']!=0)]


# In[252]:


dist_fare_1 = dist_fare.loc[(dist_fare['fare_amount']>3.0)&(dist_fare['H_Distance']==0)]


# In[253]:


dist_fare_1['H_Distance'] = dist_fare_1.apply(
lambda row: ((row['fare_amount']-2.50)/1.56), axis=1
)


# In[254]:


train.update(dist_fare_1)


# In[255]:


train.columns


# In[256]:


#not including the pickup_datetime columns as datetime columns cannot be directly used while modelling. Features need to extracted from the 
#timestamp fields which will later be used as features for modelling.
train = train.drop(['key','pickup_datetime'], axis = 1)
test = test.drop(['key','pickup_datetime'], axis = 1)


# In[257]:


x_train = train.iloc[:,train.columns!='fare_amount']
y_train = train['fare_amount'].values
x_test = test


# In[258]:


x_train


# In[259]:


y_train.shape


# In[260]:


from sklearn.ensemble import RandomForestRegressor
RF = RandomForestRegressor()
RF.fit(x_train, y_train)
y_pred = RF.predict(x_test)


# In[261]:


y_pred

