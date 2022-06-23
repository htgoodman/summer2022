#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np 
from matplotlib import pyplot as plt


# In[3]:


from marvin.tools import RSS
#row-stacked spectra "2d arrays in which each row corresponds to a 1d spectrum"


# In[4]:


rss = RSS(plateifu='11942-6104')


# In[8]:


rss


# In[42]:


#different indices [] correspond to different fibers within the galaxy (i.e. position)
#for this plateifu, the marvin web told me 
#fiberid = 164
#fiber_flux = 0.5227, 0.8605, 8.7609, 45.6182, 107.4934, 161.8557, 223.3985
#fiber_flux_ivar = 1260.1416, 6525.1445, 11.0353, 17.786, 5.8768, 0.1999, 0.3298


# In[44]:


fiber = rss[164]
fiber


# In[46]:


fiber.plot()


# In[11]:


from marvin import config
from marvin.tools import Cube


# In[12]:


cube = Cube('11942-6104')


# In[13]:


cube


# In[14]:


cube.filename


# In[15]:


remote_cube = Cube('12772-6101')


# In[16]:


remote_cube


# In[17]:


print('Target Coordindates:', cube.ra, cube.dec)
print('Header:')

# access the PRIMARY header for the current object
cube.header


# In[19]:


cube.wcs #world coordinate system, Astropy


# In[20]:


# look up the cube datmaodel
datamodel = cube.datamodel
datamodel


# In[21]:


# see what datacubes are available
print('Datacubes:')
datamodel.datacubes


# In[22]:


# see what additional spectral extensions are available
print('Spectra:')
datamodel.spectra


# In[23]:


#has three 3D datacubes (flux, dispersion, dispersion pixel) and 
#two spectra (spectral resolution and spectral resolution prepixel)


# In[24]:


print('Flux description:', datamodel.datacubes.flux.description)
print('Spectral Resolution description:', datamodel.spectra.spectral_resolution.description)


# In[25]:


#this will help access (numer of) fibers ?


# In[26]:


flux = cube.flux


# In[27]:


flux


# In[29]:


fibers = Cube.rssfibers


# In[33]:


new_search = '(z<0.1 and nsa.sersic_logmass > 11.47) or (ifu.name=19* and nsa.sersic_n < 2)'


# In[38]:


# this is the Query tool
from marvin.tools.query import Query


# In[41]:


q = Query(searchfilter=new_search)


# In[ ]:


r.results

