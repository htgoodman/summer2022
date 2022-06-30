#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import matplotlib.pyplot as plt


# In[3]:


import math
from numpy import log as ln


# Model 1: Saturated Exponential. Assumes all neutral gas in galactic disc follows an exponential surface density profile (i.e. gas profile comprised of HI + H_2)

# the following are from Model 0: surface density parameters:

# In[6]:


#HI surface density at the galaxy center
epsilon_0 = 10.0 #M_solar / pc^2


# In[ ]:


#HI surface density UNIT
epsilon_c = 1.0 #M_solar / pc^2


# In[7]:


def epsilon_HI(r): 
    if r <= r_b: 
        epsilon_HI(r) = epsilon_0
    if r > r_b:
        epsilon_HI(r) = epsilon_0 * math.exp


# In[ ]:





# In[ ]:




