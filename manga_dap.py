#!/usr/bin/env python
# coding: utf-8

# In[ ]:


## some of this is review; some is quite new


# In[1]:


import numpy as np
from astropy.io import fits
from matplotlib import pyplot as plt


# In[3]:


##next I am using a fits file that manga suggests 


# In[4]:


# This assumes the MAPS file is in the current directory.  If that's not
# true, replace '' below with the directory containing the data file.
dir = ''
hdu = fits.open(dir+'manga-7443-12703-MAPS-HYB10-MILESHC-MASTARSSP.fits.gz')


# In[6]:


#hdu


# In[7]:


hdu.info()


# In[8]:


hdu['EMLINE_GFLUX'].data.shape #Halpha emission line / galactic flux
#given as (velocity?) "channel", y-position, x-position.


# In[9]:


hdu['EMLINE_GFLUX'].header #gives details for the extension of Halpha flux


# In[10]:


flux_halpha = hdu['EMLINE_GFLUX'].data[23]
#defines this as a pipeline of sorts?


# In[11]:


emline = {}
for k, v in hdu['EMLINE_GFLUX'].header.items():
    if k[0] == 'C':
        try:
            i = int(k[1:])-1
        except ValueError:
            continue
        emline[v] = i


# In[12]:


flux_halpha = hdu['EMLINE_GFLUX'].data[emline['Ha-6564']]


# In[13]:


plt.clf() #need to look into this extension!
plt.imshow(hdu['EMLINE_GFLUX'].data[emline['Ha-6564']], origin='lower', interpolation='nearest',
           cmap='inferno')
plt.colorbar(label=r'H$\alpha$ Flux [$10^{-17}$ erg/s/cm$^2$/spaxel]')
plt.show()


# In[14]:


mask_extension = hdu['EMLINE_GFLUX'].header['QUALDATA']


# In[ ]:




