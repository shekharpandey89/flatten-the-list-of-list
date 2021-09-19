#!/usr/bin/env python
# coding: utf-8

# # Method 1: Using for loop

# In[1]:


lst = [[30,7],[8,9],[30,7],[8,9]]
flatten_list = []
for i in lst:
  for item in i:
    flatten_list.append(item)
print("list before flattening", lst)
print ("flattened list: ",flatten_list)


# # Method 2: Using a list comprehension

# In[16]:


lst = [[30,7],[8,9],[30,7],[8,9]]
print("list before flattening", lst)
print ("list after flattening",[item for i in lst for item in i])


# # Method 3: Using  flatten() Method

# In[6]:


from iteration_utilities import flatten
lst = [[30,7],[8,9],[30,7],[8,9]]
print(list(flatten(lst)))


# In[7]:


from iteration_utilities import flatten
lst = [[30,7],[8,9],[30,7],[8,9],[[2]]]
print(list(flatten(lst)))


# # Method 4: Using deepflatten() Method

# In[8]:


from iteration_utilities import deepflatten
lst = [[30,7],[8,9],[30,7],[8,9],[ [200 ] ]]
print("list lst before flattening", lst)


# In[9]:


flatten_lst = list(deepflatten(lst))
print("list lst after flattening", flatten_lst)


# # Method 5: Using pandas flatten method

# In[17]:


from pandas.core.common import flatten
lst = [[30,7],[8,9],[30,7],[8,9],[[2]]]
print("list before flattening", lst)
print ("flattened list: ",list(flatten(lst)))


# # Method 6: Using matplotlib flatten method

# In[18]:


from matplotlib.cbook import flatten
lst = [[30,7],[8,9],[30,7],[8,9],[[2]]]
print("list before flattening", lst)
print ("flattened list: ",list(flatten(lst)))


# # Method 7: Using unipath flatten method

# In[19]:


import unipath
from unipath.path import flatten
lst = [[30,7],[8,9],[30,7],[8,9],[[2]]]
print("list before flattening", lst)
print ("flattened list: ",list(flatten(lst)))


# # Method 8: Using setuptools flatten method

# In[21]:


from setuptools.namespaces import flatten
lst = [[30,7],[8,9],[30,7],[8,9],[[2]]]
print("list before flattening", lst)
print ("flattened list: ",list(flatten(lst)))


# # Method 9: Using itertools.chain()

# In[22]:


import itertools
lst = [[30,7],[8,9],[30,7],[8,9],[[2]]]
print("list lst before flattening", lst)
flatten_lst = list((itertools.chain.from_iterable(lst)))
print("list li after flattening", flatten_lst)


# In[23]:


import itertools
lst = [[30,7],[8,9],[30,7],[8,9],[[2]]]
print("list lst before flattening", lst)
flatten_lst = list((itertools.chain(*lst)))
print("list li after flattening", flatten_lst)


# # Method 10: Using numpy.ravel () method

# In[38]:


import numpy as np 
lst = np.array([[30,7],[8,9],[30,7],[8,9]])
flatten_lst = lst.ravel()
print("list before flattening", lst)
print ("flattened list: ",list(flatten(lst)))


# # Method 11: Using numpy.reshape () method

# In[37]:


import numpy as np 
lst = np.array([[30,7],[8,9],[30,7],[8,9]]) 
flatten_lst = lst.reshape(-1) 
print("list before flattening", lst)
print ("flattened list: ",list(flatten(lst)))


# # Method 12: Using numpy flatten () method

# In[44]:


import numpy as np 
lst = np.array([[30,7],[8,9],[30,7],[8,9]]) 
flatten_lst = lst.flatten() 
print("list before flattening", lst)
print ("flattened list: ",list(flatten(lst)))


# # Method 13: Using numpy.concatenate () method

# In[41]:


import numpy as np 
lst = np.array([[30,7],[8,9],[30,7],[8,9]]) 
flatten_lst = list(np.concatenate(lst))
print("list before flattening", lst)
print ("flattened list: ",list(flatten(lst)))


# # Method 14: Using numpy flat method

# In[43]:


import numpy as np 
lst = np.array([[30,7],[8,9],[30,7],[8,9]]) 
flatten_lst = list(lst.flat)
print("list before flattening", lst)
print ("flattened list: ",list(flatten(lst)))


# In[ ]:




