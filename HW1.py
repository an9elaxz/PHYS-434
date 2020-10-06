#!/usr/bin/env python
# coding: utf-8

# In[1]:


# import the libraries
get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import scipy
from scipy import stats

#this sets the size of the plot to something useful
plt.rcParams["figure.figsize"] = (15,10)


# In[2]:


# create a gaussian distribution of 100k points using the stats package from scipy
d = stats.norm.rvs(loc = 5., scale = 0.01, size = 100000) # loc sets the mean for gaus, rvs stands for random varibles


# In[3]:


fig, ax = plt.subplots(1, 1) # create a figure
ax.hist(d, 50, density=True) # fill the figure with a hist & gaus distribution d
plt.tick_params(labelsize = 24) # sets tick parameter for the plot, in this case, the label size
plt.xlim([4.95,5.05]) # sets rage for x axis
x = np.linspace(4.95,5.05,1000) # create an array with numpy that contains equally spaced 1000 points between 4.95 and 5.05
ax.plot(x,stats.norm.pdf(x,loc = 5., scale = 0.01),linewidth = 8,alpha = 0.7) # alpha adjusts the transparency of a graph plot
plt.show()


# In[4]:


ax = plt.hist(d,50)
plt.yscale('log') # sets y axis to log scale
plt.tick_params(labelsize = 24)
plt.xlim([4.95,5.05])
plt.show()


# In[5]:


fig, ax = plt.subplots(1, 1)
ax.hist(d,50, density=True)
plt.yscale('log')
plt.tick_params(labelsize = 24)
plt.xlim([4.95,5.05])
x = np.linspace(4.95,5.05,1000)
ax.plot(x,stats.norm.pdf(x,loc = 5., scale = 0.01),linewidth = 8,alpha = 0.7)
plt.show()


# In[ ]:




