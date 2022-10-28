#!/usr/bin/env python
# coding: utf-8

# Write a NumPy program to convert a list of numeric values into a
# one-dimensional NumPy array

# In[1]:


import numpy as np


# In[2]:


a1=[22,43,27,87,90,34]
n1=np.array(a1)


# In[4]:


n1


# Write a NumPy program to create a 4x4 matrix with values ranging from 7
# to 15.

# In[14]:


a2=np.random.randint(7,16, size=(4,4))


# In[15]:


a2


# Write a NumPy program to create a null vector of size 10 and update the
# sixth value to 11.

# In[17]:


a3=np.zeros(10)


# In[18]:


a3


# In[19]:


a3[5]=11


# In[20]:


a3


# Write a NumPy program to reverse an array (first element becomes last).
# 

# In[21]:


a4=np.arange(0,20)


# In[22]:


a4


# In[23]:


a5=a4[::-1]


# In[24]:


a5


# Write a NumPy program to create a 2d array with 1 on the border and 0
# inside.

# In[26]:


a6=np.ones((4,4))


# In[27]:


a6


# In[28]:


a6[1:-1,1:-1]=0


# In[29]:


a6


# Write a NumPy program to create a 8x8 matrix and fill it with a
# checkerboard pattern.
# 

# In[35]:


a7=np.zeros((8,8),dtype=int)


# In[36]:


a7


# In[38]:


a7[1::2,::2] = 1
a7[::2,1::2] = 1


# In[39]:


a7


# Write a NumPy program to append values to the end of an array.

# In[42]:


a8=np.random.randint(100, size=(20))


# In[43]:


a8


# In[45]:


a9=np.append(a8, 45)


# In[46]:


a9


# Write a NumPy program to convert the values of Centigrade degrees into Fahrenheit degrees and vice versa. Values are stored into a NumPy array

# In[49]:


C=(0,45,100,35)
c1=np.array(C)
f = (9 * c1 / 5 + 32)
f


# Write a NumPy program to find the number of elements of an array, length
# of one array element in bytes and total bytes consumed by the elements

# In[53]:


a10 = np.array([16,22,53,76], dtype=np.float64)
a10


# In[52]:


("Size of the array: ", a10.size)


# In[54]:


("Length of one array element in bytes: ", a10.itemsize)


# In[55]:


("Total bytes consumed by the elements of the array: ", a10.nbytes)


# Write a NumPy program to test whether each element of a 1-D array is
# also present in a second array

# In[60]:


a11 = np.array([0, 10, 20, 40, 60])
a12 = np.array([0, 40, 90, 20, 50])

a13=np.in1d(a11, a12)
a13


# Write a NumPy program to create an array of ones and an array of zeros.

# In[62]:


a14=np.ones((4,4))
a14


# In[63]:


a15=np.zeros((4,4))
a15


# Write a NumPy program to create a new shape to an array without
# changing its data

# In[65]:


a16=np.random.randint(10,100, size=(20))
a16


# In[68]:


a17 = a16.reshape(5, 4)
a17


# In[70]:


a18=a16.reshape(2,2,5)
a18


# Write a NumPy program to change the data type of an array

# In[73]:


a19=a16.astype(float)
a19


# Write a NumPy program to create a new array of 3*5, filled with 2

# In[74]:


a20=np.random.randint(2,3, size=(3,5))
a20


# Write a NumPy program to create a 3-D array with ones on a diagonal
# and zeros elsewhere

# In[85]:


a23=np.eye(5)
a24=np.eye(5)
a25=np.eye(5)
a26=np.array(((a23),(a24),(a25)))
a26


# Write a NumPy program to create a 1-D array of 20 element spaced
# evenly on a log scale between 2. and 5., exclusive.

# In[93]:


a27=np.random.uniform(2.,5., size=(20))
a27


# Write a NumPy program to get the number of nonzero elements in an
# array

# In[99]:


a28=np.random.randint(0,100, size=(30))
a28


# In[105]:


np.count_nonzero(a28>1)


# Write a NumPy program (using NumPy) to sum of all the multiples of 3 or 5 below 100

# In[108]:


a29=np.arange(0,100,3)
a30=np.arange(0,101,5)
sum(a29)


# In[109]:


sum(a30)


# In[ ]:




