#Loading the mongolite library
library(mongolite)

#establishing a connection with the mongoDB & selecting a collection from a database, default port = 27017
selected_collection = mongo(db = 'Assignment8_R', collection = 'IMDB_Data_R', url = "mongodb://localhost")

#Reading in the CSV file
library(readr)
imdb_data = read.csv("IMDB_data.csv", header = FALSE)

#Inserting into the DB
selected_collection$insert(imdb_data)
