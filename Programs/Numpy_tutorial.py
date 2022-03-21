
# coding: utf-8

# In[15]:


import numpy as np
import sys


# In[24]:


l=range(100)
l


# In[17]:


array=np.arange(100)


# In[18]:


array


# In[19]:


sys.getsizeof(1)*len(l) #finding the size occupied by the native python list


# In[20]:


array.size #gives the size of the array


# In[21]:


array.itemsize  # gives the size of single item on array


# In[22]:


array.size * array.itemsize  #total memory used by array


# In[25]:


array.dtype


# In[33]:


a=np.array(np.arange(100),dtype='int64')


# In[34]:


a.size*a.itemsize


# In[40]:


a=np.array(np.arange(100),dtype='int32')


# In[42]:


a.size*a.itemsize


# In[70]:


array_2 = np.array([[1,2,765],[6,77,55423],[12,3434,4343],[34343,432,90]])   #declaring array

array_1= np.array([12,3434,4343,34343,432,90])


# In[71]:


array_2.ndim   #ndim gives the dimension of array
 


# In[72]:


array_1.ndim


# In[73]:


array_1


# In[74]:


array_2.shape  # gives the shape of the array


# In[75]:


array_2.reshape(3,4)  # reshapes the array to 3,4


# ravel() - coverts n dimensional array to 1 dimension

# In[80]:


new_array=array_2.ravel()


# In[81]:


new_array.shape


# In[82]:


new_array.ndim


# # Place Holders in numpy

# In[86]:


np.zeros([5,5], dtype='float64')  # creates 5 * 5 array with elements 0


# In[87]:


np.ones([5,3], dtype='int32')


# In[91]:


np.ones(5) # creates one dimensional placeholders of value 1


# # np.linspace(start_bit, end_bit, no_of_elements)

# In[97]:


np.linspace(1,20, 12)  #creates linearly placed elements


# # numpy operations

# In[99]:


a=np.arange(1,11).reshape(5,2)


# In[100]:


a


# In[101]:


a.max()  # maximum element in the array


# In[107]:


a.min()  # minimum element in the array


# In[103]:


a.sum()  # sum of all elements in the array

# axis = 1 refers rows

# axis = 0 refers columns
# In[104]:


a.sum(axis=1)  # here sum is calculated row - wise


# In[106]:


a.sum(axis=0)  # here sum is calculated column - wise


# # Numpy Mathematical

# In[114]:


a = np.arange(5,11).reshape(3,2)


# In[115]:


b = np.arange(15,21).reshape(3,2)


# In[116]:


a


# In[117]:


b


# In[118]:


a + b # does element wise addition


# In[119]:


a - b


# In[120]:


a * b  # element wise


# In[122]:


a.dot(b.reshape(2,3))  # matrix multiplication


# In[124]:


np.sqrt(a)  # square root element wise


# In[126]:


np.std(b)  # gives the standard deviation


# # slicing

# In[127]:


a= np.arange(5)


# In[128]:


a


# In[129]:


a[0:3]  # end point slicing funcs is same as range.


# In[130]:


a[-1] # prints last element


# In[131]:


a[:-1] # excludes last element


# In[136]:


a[::-1]  # the third argument is stepsize


# In[140]:


a = np.array([[344,565,453423],['Bits','with','Bits'],[12,53344,4343]])


# In[141]:


a

a[rows,columns] 
# In[147]:


a[0:2,1]    # Here row ranges from 0 to 1 and column 1 (index starts from zero)

#final output will be the intersection of rows and columns


# In[149]:


a[-1]  #prints last row


# In[151]:


a[:,-1]  #prints last column


# In[ ]:


# Accessing array via loop


# In[152]:


for row in a:
    print(row)  # printing each row on single iteration


# In[153]:


for value in a.ravel():  # printing each value of array per iteration
    print(value)


# In[155]:


for value in a.flat:   # same as ravel function
    print(value)


# In[196]:


a = np.array([[344,565,453423],['Bits','with','Bits'],[12,53344,4343]])


# In[189]:


a


# In[188]:


for value in np.nditer(a,order='C'):   # prints the element in row-wise
    print (value)


# In[190]:


for value in np.nditer(a,order='F'):   # prints the element in column-wise usually called as Fortan order
    print (value)


# In[197]:


a


# In[192]:


b=np.array(['Hello','World','Good Day']).reshape(3,1)


# In[193]:


b


# In[195]:


for x,y in np.nditer([a,b]):  # adding elements row wise
    print(x,y)


# In[ ]:


# Note : To perform above operation, two array must be compatible with each other on shape 


# # Array stacking

# In[157]:


a= np.arange(0,10).reshape(5,2)
b= np.arange(20,30).reshape(5,2)


# In[159]:


a


# In[160]:


b


# In[162]:


np.vstack((a,b))  # Array a has been stacked on b


# In[163]:


np.hstack((a,b))  # adding array b to a on adjacent 


# # Array Splitting

# In[165]:


a=np.arange(0,30).reshape(2,15)


# In[166]:


a


# In[170]:


new_array=np.hsplit(a,3) # divides the array into 3 parts adjacent wise


# In[171]:


new_array[0]


# In[172]:


new_array[1]


# In[173]:


new_array[2]


# # Boolean in array

# In[179]:


a


# In[176]:


condition = a >10


# In[180]:


condition  # returns true for the values > 10


# In[184]:


a[condition]=0


# In[185]:


a   # the value is changed to 0 for all true condition

