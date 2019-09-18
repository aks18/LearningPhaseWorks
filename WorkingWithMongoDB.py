#!/usr/bin/env python
# coding: utf-8

# In[3]:


#Load libraries
import pandas as pd
import os
import pymongo as pymongo
from pymongo import MongoClient
import pprint
import json


# In[4]:


# Connect to the MongoDB, change the connection string per your MongoDB environment
Channel = MongoClient(port=27017)


# In[5]:


Channel


# In[13]:


#Selecting a database, if there is not one with this name, it creates a new one, I guess
working_db = Channel.Assignment8Answers


# In[8]:


#Loading the data to store into the database, using the same previous IMDB file
imdbData = pd.read_csv("IMDB_data.csv", encoding = "latin1")


# In[11]:


#Converting the DataFrame to JSON, as MongoDB stores only in JSON format
imdbData_json = json.loads(imdbData.T.to_json()).values()


# In[12]:


#imdbData_json


# In[16]:


#Using the selected DB, picking a collection (if non-existant, it creates one) & inserting the imdb_json data
#working_db.IMDB_Data.drop()
working_db.IMDB_Data.insert(imdbData_json)


# In[18]:


#Returns the collections in the present selected DB
working_db.collection_names()


# In[19]:


#Selecting any particular collection
selected_collection = working_db.IMDB_Data


# In[20]:


selected_collection


# In[21]:


#Extract 1st document in the selected collection
selected_collection.find_one()


# In[22]:


#print the selected collection in proper sense
pprint.pprint(selected_collection.find_one())


# In[24]:


pprint.pformat(selected_collection.find_one())
