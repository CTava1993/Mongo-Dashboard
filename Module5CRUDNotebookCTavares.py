#!/usr/bin/env python
# coding: utf-8

# In[87]:


from pymongo import MongoClient
from bson.objectid import ObjectId

# Christian Tavares || CS340 Client/Server Development 2024 || 9/29/2024
# -------------------------------------------------------------------------
# This file is made to be an example of how to use CRUD to read and write in
# the aac database within Mongo. It is run inside of Jupyter Notebook.

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, username, password, host, port, db, col):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections.
        # This is hard-wired to use the aac database, the 
        # animals collection, and the aac user.
        # Definitions of the connection string variables are
        # unique to the individual Apporto environment.
        #
        # You must edit the connection variables below to reflect
        # your own instance of MongoDB!
        #
        # Connection Variables
        #
        USER = username # updated username
        PASS = password # updated password
        # HOST = 'nv-desktop-services.apporto.com'
        HOST = host
        # PORT = 30728
        PORT = port
        # DB = 'aac'
        DB = db
        # COL = 'animals'
        COL = col
        #
        # Initialize Connection
        #
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]

# Create method to implement the C in CRUD.
    def create(self, data):
        if data is not None:
            self.database.animals.insert_one(data)  # data should be dictionary
            return "True"
        else:
            raise Exception("Nothing to save, because data parameter is empty")
            return "False"

# Create method to implement the R in CRUD.
    def read(self, data):
        if data is not None:
            results = self.database.animals.find(data)  # data should be dictionary
            data = list(results)
            
            return data
        else:
            results = self.database.animals.find({})  # data should be dictionary
            return list(results)
        
# Update method to implement the U in CRUD.
    def update(self, data, setData, returnData):
        if data is not None:
            self.database.animals.update_many(data, setData) # data should be dictionary
            results = self.database.animals.find(returnData) 
            data = list(results)
            
            return data
        else:
            results = self.database.animals.find({})  # data should be dictionary
            return list(results)
    
# Delete method to implement the D in CRUD.
    def delete(self, data):
        if data is not None:
            myData2 = crud.read(data) # data should be dictionary
            self.database.animals.delete_many(data) # data should be dictionary
            return myData2
        else:
            return "Nothing was deleted. ."
