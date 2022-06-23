#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np 
from matplotlib import pyplot as plt
from marvin.tools import RSS
from marvin.tools import Cube
from marvin import config


# In[4]:


cube = Cube('11942-6104')


# In[5]:


cube


# In[6]:


cube.wcs #world coordinate system, Astropy


# In[7]:


spaxel = cube.getSpaxel(0,0)
spaxel.flux.plot()


# In[8]:


spaxel=cube.getSpaxel(ra=249.083630374,dec=39.9462259106)


# In[9]:


spaxel.flux.plot()


# In[ ]:




