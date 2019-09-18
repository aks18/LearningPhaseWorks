#!/usr/bin/env python
# coding: utf-8

# # Assignment 3 - Question 2

# In[2]:


import pandas as pd
import os
import numpy as np


# In[28]:


d = pd.read_csv("IMDB_data.csv", encoding="cp1252")
d
#works fine even with encoding = 'iso-8859-1', 'cp1252', 'iso-8859-15', 'latin1'
#gives error on encoding = 'utf-8', 'utf-16'


# In[26]:


#==================  2a  =====================
dataIMDB = pd.read_csv("IMDB_data.csv", header = [0], encoding = "ISO-8859-15", skiprows = [2])
dataIMDB


# In[187]:


#==================  2b & 2d  ======================
#Counting number of occurances of each Genre using groupby function. 
#That sorts as well
a = pd.DataFrame(dataIMDB.groupby(dataIMDB.Genre).Plot.nunique())
#Making the index the Genre columns
a['Genre'] = a.index
#Renaming the columns in the data frame
a.columns = ['Counts', 'Genre']
#Resetting the indexes
a.index = range(len(a))
#Realigning the columns
a = a[['Genre', 'Counts']]
#Inserting the index column
a.insert(0, 'ID', range(1, 1+len(a)))
uniq_genre = a
#Freeing up space
del a
uniq_genre


# In[205]:


#==========Another way to do 2b & 2d ===================
a = dataIMDB.Genre.value_counts()
a = pd.DataFrame(a)
a['Genres'] = a.index
a.columns = ['Counts', 'Genre']
a.index = range(1, 1+len(a))
a = a.sort_values(by='Genre')
a.index = range(len(a))
a = a[['Genre', 'Counts']]
a.insert(0, 'ID', range(1, 1+len(a)))
a


# In[206]:


dataIMDB.describe()


# In[233]:


#==================  2c  ======================
#Copying data to avoid rerunning the kernel
x = dataIMDB
#Converting imdbRating & imdbVotes from str type to numeric type.
#errors = coerce - forces uncompatible data to be parsed to NaN, and not raise an error
#astype() gives errors. For error argument, it has only 'ignore' & 'raise' values. So doesn't work
x.imdbRating = pd.to_numeric(x.imdbRating, errors='coerce')
x.imdbVotes = pd.to_numeric(x.imdbVotes, errors='coerce')
type(x.imdbRating[2]), type(x.imdbVotes)


# In[238]:


#=================  2e  =======================
x['SquaredDiff'] = (x.imdbRating - x.imdbVotes)**2
x


# In[246]:


x = x.astype(object)
type(x.Language[1])


# In[248]:


#==============  2c  ==============
#Converting Language from categorical to numeric type using LabelEncoder
from sklearn.preprocessing import LabelEncoder
lblenc = LabelEncoder()
x.Language = lblenc.fit_transform(x.Language)
x


# # DONE
