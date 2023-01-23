#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np


# In[51]:


a=np.array([[34,45,3,45,6,77,67,56]]) 


# In[52]:


a


# In[53]:


a.reshape(4,2)


# In[54]:


a.shape


# In[55]:


a.ndim


# In[56]:


a.itemsize


# In[59]:


b=np.arange(100,200,10)


# In[60]:


b=arr.reshape(5,2)


# In[61]:


b


# In[64]:


c= np.array([[11,22,33],[44,55,66], [77,88,99]])


# In[65]:


c[:,-1]


# In[79]:


d=np.array([[3,6,9,12],[15,18,21,24],[27,30,33,36],[39,42,45,48],[51,54,57,60]])


# In[85]:


d


# In[81]:


e=np.array([0,1,2,3,4,5,6,7,8,9])


# In[83]:


e[e%2==1]


# In[88]:


f=np.zeros(10)


# In[89]:


f


# In[90]:


a.size


# In[92]:


g=np.arange(10,49)


# In[93]:


g


# In[99]:


h=np.eye(3,3,3)


# In[100]:


h


# In[103]:


i=np.random.random((3,3,3))


# In[104]:


i


# In[105]:


print(np.__version__)
print(np.show_config())


# In[129]:


f=np.zeros(10)


# In[130]:


f


# In[131]:


f[6]=11


# In[132]:


f


# In[136]:


k=np.arange(1,7)


# In[137]:


k


# In[138]:


k=k[::-1]


# In[140]:


k


# In[ ]:




