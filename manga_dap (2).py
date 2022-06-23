#!/usr/bin/env python
# coding: utf-8

# In[ ]:


## some of this is review; some is quite new


# In[3]:


import numpy as np
from astropy.io import fits
from matplotlib import pyplot as plt


# In[4]:


##next I am using a fits file that manga suggests 


# In[11]:


# This assumes the MAPS file is in the current directory.  If that's not
# true, replace '' below with the directory containing the data file.
dir = ''
hdu = fits.open(dir+'manga-11942-6104-LOGRSS.fits.gz')


# In[7]:


from marvin.tools.maps import Maps


# In[9]:


maps = Maps(plateifu='11942-6104')
print(maps)
# get an emission line map
haflux = maps.emline_gflux_ha_6564
values = haflux.value
ivar = haflux.ivar
mask = haflux.mask
haflux.plot()


# In[10]:


maps = Maps(plateifu='11942-6104')
print(maps)
# get an emission line map
specindex = maps.specindex_d4000
values = specindex.value
ivar = specindex.ivar
mask = specindex.mask
specindex.plot()


# In[25]:


hdu.info()


# In[22]:


hdu['SPECRES'].data #Halpha emission line / galactic flux
#given as (velocity?) "channel", y-position, x-position.


# In[23]:


hdu['SPECRES'].header #gives details for the extension of Halpha flux


# In[26]:


gvel_map = maps.emline_gvel_h11_3771
#defines this as a pipeline of sorts?


# In[30]:


gvel_map.data.shape


# In[12]:


#flux_halpha = hdu['EMLINE_GFLUX'].data[emline['Ha-6564']]


# In[31]:


gvel_map.plot()


# In[14]:


mask_extension = hdu['EMLINE_GFLUX'].header['QUALDATA']


# In[15]:


masked_image = np.ma.array(hdu['EMLINE_GFLUX'].data[emline['Ha-6564']],
                           mask=hdu[mask_extension].data[emline['Ha-6564']]>0)
plt.clf()
plt.imshow(masked_image, origin='lower', interpolation='nearest', cmap='inferno')
plt.colorbar(label=r'H$\alpha$ Flux [$10^{-17}$ erg/s/cm$^2$/spaxel]')
plt.show()


# In[ ]:




