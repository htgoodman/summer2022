#!/usr/bin/env python
# coding: utf-8

# In[10]:


import numpy as np 
from matplotlib import pyplot as plt
from marvin.tools import RSS
from marvin.tools import Cube
from marvin import config


# In[11]:


cube = Cube('11942-6104')


# In[12]:


cube


# In[13]:


cube.wcs #world coordinate system, Astropy


# In[14]:


spaxel = cube.getSpaxel(0,0)
spaxel.flux.plot()


# In[15]:


spaxel=cube.getSpaxel(ra=249.083630374,dec=39.9462259106)


# In[16]:


spaxel.flux.plot()


# In[17]:


cube2 = Cube('9187-9101')


# In[18]:


cube2


# In[19]:


cube2.wcs #world coordinate system, Astropy


# In[20]:


spaxel2 = cube2.getSpaxel(0,0)
spaxel2.flux.plot()


# In[21]:


maps = cube2.getMaps()


# In[40]:


hamap = maps.getMap('emline_sflux',channel='ha_6564')
hamap.plot()


# In[25]:


import matplotlib.pyplot as plt
from marvin.tools.maps import Maps
import marvin.utils.plot.map as mapplot
from marvin.tools.image import Image
plt.style.use('seaborn-darkgrid')  # set matplotlib style sheet


# In[28]:


image = Image(plateifu='9187-9101')
image.plot()


# In[29]:


image = Image(plateifu='11942-6104')
image.plot()


# In[31]:


maps = Maps(plateifu='9187-9101')


# In[33]:


#maps.datamodel


# In[34]:


ha = maps.emline_gflux_ha_6564


# In[35]:


fig, ax = ha.plot()


# In[36]:


gas_vfield = maps.emline_gvel_ha_6564
fig, ax = gas_vfield.plot()


# In[37]:


#this shouldn't change my velocity field too much, because it looks 
#as though almost all regions have S/N > 10
mask_snr10 = (ha.snr < 10) * ha.pixmask.labels_to_value('DONOTUSE')
mask = ha.mask | mask_snr10
fig, ax = mapplot.plot(dapmap=gas_vfield, value=gas_vfield.value, mask=mask)


# In[39]:


#from documentation fig, axs = plt.subplots(NUMBER, sharex=True, sharey=True)
fig, axs = plt.subplots(16, sharex=True, sharey=True)
fig.suptitle('H-alpha Spectra for 16 MaNGA Galaxies')

#for i in axs:
 #   axs[i].plot
#revisit this later to implement a loop instead of calling subplots individually


# In[41]:


plateifus = ['9187-9101', '7965-6102', '9870-12705', '9187-1901', '9187-6104', '8998-12703', '8998-12704', '11948-1901']

for i in plateifus: 
    maps = Maps(plateifu= i)
    ha = maps.emline_gflux_ha_6564
    fig, ax = ha.plot()


# In[ ]:



#maps = Maps(plateifu='9187-9101')
#ha = maps.emline_gflux_ha_6564
#fig, ax = ha.plot()

#or 


#hamap = maps.getMap('emline_sflux',channel='ha_6564')
#hamap.plot()

