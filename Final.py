#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
from pandas import *
from scipy import stats

data = read_csv('uscoviddata.csv')

data.plot.bar(y=['death','positive','totalTestResults','hospitalizedCurrently'], x='date',subplots=True, layout=(2,2))
data.plot.bar(y=['deathIncrease','positiveIncrease','totalTestResultsIncrease','hospitalizedIncrease'], x='date',subplots=True, layout=(2,2))


# In[ ]:
