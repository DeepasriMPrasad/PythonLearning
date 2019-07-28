#!/usr/bin/env python
# coding: utf-8

# ## Numpy Assignment

# (Q). Create an array using the method 1. array 2. arange 3. linspace

# In[11]:


# 1.array
import numpy as np
a = np.array([1,2,3,4])
print("simple numpy array")
print(a)
print(type(a))

#2.arange
b = np.array(np.arange(1,10,2))
print("using arange")
print(b)

#linspace
c=np.array(np.linspace(4,9,5))
print("using linspace")
print(c)


# (Q) Identify the shape and dimensions of an array 

# In[19]:


a = np.array([[1,2,3,4],[5,6,7,8]])
print(a)
print("shape: {}".format(a.shape))
print("dimension: {}".format(a.ndim))
a.ndim


# (Q) Replace the values which are multiples of 5 by -1 using fancy indexing in [1,5,10,4,15,20,7,35]

# In[22]:


fancyarray = np.array([1,5,10,4,15,20,7,35])
mask = (fancyarray % 5 == 0)
fancyarray[mask] = -1
print(fancyarray)


# (Q) Create a array and find out the sum of the elements 

# In[23]:


mysumarray = np.array([1,5,10,4,15,20,7,35])
print(mysumarray.sum())


# (Q) Reshape an array np.array([1, 2, 3, 4], ndmin=2) using ravel and identify the shape, dimensions and write your conclusions

# In[41]:


oldarray = np.array([1, 2, 3, 4], ndmin=2) 
print(oldarray)
print(oldarray.ndim)
print(oldarray.shape)
#ravel - flattens out the array structure to 1-Dimension
newarray = oldarray.ravel()
print(newarray)
print(newarray.ndim)
print(newarray.shape)
#We can reshape the same
rearray = newarray.reshape((1,4))
print(rearray)
print(rearray.ndim)
print(rearray.shape)


# (Q) How to remove from one array those items that exist in another?
# a = np.array([1, 2, 3, 4, 5])
# b = np.array([5, 6, 3, 1, 4])

# In[115]:


a= np.array([1, 2, 3, 4, 5])
b = np.array([5, 6, 3, 1, 4])
#z = (a) ^ (a | b))
x = np.setdiff1d( a, b )
y = np.setdiff1d( b, a )
print(x)
print(y)
#print(z)




# ## Pandas 

# (Q) How to combine two series into a dict
# 
# ser1 = pd.Series(list('abcedfghijklmnopqrstuvwxyz'))
# ser2 = pd.Series(np.arange(26))

# In[96]:


import pandas as pd

ser1 = pd.Series(list('abcedfghijklmnopqrstuvwxyz'))
ser2 = pd.Series(np.arange(26))
#print("Series1 {}".format(ser1))
#print("Series2 {}".format(ser2))
print("Dictionary")
d = pd.Series(ser2.values, index=ser1)
print(d.to_dict())
print("Data Frame")
dataf = pd.DataFrame.from_dict(d)
print(dataf)


# (Q) How to get the minimum, 25th percentile, median, 75th, and max of a numeric series?
# 
# a = pd.Series(np.random.normal(10, 5, 25))

# In[157]:


a = pd.Series(np.random.normal(10, 5, 25))
print("Series")
print(a)
print("------------------------")
print("min: {}".format(a.min()))
print("25th percentile: {}".format(np.percentile(a, 25)))
print("median: {}".format(a.median()))
print("75th percentile: {}".format(np.percentile(a, 75)))
print("max: {}".format(np.max(a)))
#print(a.describe()) #toverify


# (Q) How to convert a numpy array to a dataframe of given shape?
# a = pd.Series(np.random.randint(1, 10, 35))

# In[117]:


a = pd.Series(np.random.randint(1, 10, 35))
print("Series")
print(a)
print("Data Frame")
data = a.to_frame() 
print(data)


# (Q) How to calculate the number of characters in each word in a series?
# series = pd.Series(['how', 'to', 'kick', 'ass?'])

# In[146]:


series = pd.Series(['how', 'to', 'kick', 'ass?'])
print(series)
print("Series-CharCount")
print(series.str.len())


# (Q) Import csv file using pd.read_csv method, 
# Use the weather_data.csv from the pandas folder  

# In[147]:


df = pd.read_csv('weather_data.csv')
print(df)

'''
day  temperature  windspeed  event
0  1/1/2017           32          6   Rain
1  1/2/2017           35          7  Sunny
2  1/3/2017           28          2   Snow
3  1/4/2017           24          7   Snow
4  1/5/2017           32          4   Rain
5  1/6/2017           31          2  Sunny
'''


# (Q) Obtain the columns, index and shape of the above data frame. 

# In[155]:



print(list(df.columns))
print(df.index)
print(df.shape)


# (Q) Use describe method on the dataframe and write your conclusion 

# In[163]:


print(df.describe(include='all'))

# provides Statistical summary of data frame.
'''
Describe method is useful to get descriptive summary statistics like average, standard deviation,
from dataframe, which is useful to understand data distribution of each column.

'''

