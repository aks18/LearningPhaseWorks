#no need of semi-colons -- ignore that habit

#===================  1a  =========================
#----------- 1 way of reading CSV------------
#loading the necessary library to include the functions
library(readr)
#reading the csv file
dataIMDB = read_csv("IMDB_data.csv")
#dropping the 2nd row completely with all the columns
dataIMDB = dataIMDB[-2,]
#dataIMDB = data.frame(dataIMDB)

#------------ 2nd way to reading CSV --------------
dataIMDB2 = read.csv("IMDB_data.csv", header = F, as.is = T)  #as.is = T, avoids all the columns from being converted to factor while taking input
#Making 1st column the header
colnames(dataIMDB2) = as.character(unlist(dataIMDB2[1,]))
#Removing the 1st column (header) & 3rd column
dataIMDB2 = dataIMDB2[-c(1, 3),]

#===================  1b & 1d  =========================
#------------Working with dataIMDB----------------
#Making a table of the Genre -> that will include all the unique Genres & its count.
#Then converting it into a data frame
uniq_genres = data.frame(table(dataIMDB$Genre))
#Giving column names to the the columns of the dataframe
colnames(uniq_genres) = c("Genre", "Count")
#Adding the index column
uniq_genres$ID = 1:nrow(uniq_genres)
#Rearranging the columns in the data frame. Bcoz new column gets added in the end. 
#So bringing ID to the first column
uniq_genres = uniq_genres[, c(3, 1, 2)]
#Getting the number of unique Genre
numUniqGenre = length(unique(dataIMDB$Genre))
#No need to sort the Genre by name. As in table, the data is already sorted out

#-------------Working with dataIMDB2---------------
#Converting the Character type of Genre to Factor type, before finding unique values
dataIMDB2$Genre = as.factor(dataIMDB2$Genre)
uniq_genres2 = data.frame(table(dataIMDB2$Genre))
colnames(uniq_genres2) = c("Genre", "Count")
uniq_genres2$ID = 1:nrow(uniq_genres2)
uniq_genres2 = uniq_genres2[, c(3, 1, 2)]
numUniqGenre2 = length(unique(dataIMDB2$Genre))
#No need to sort the Genre by name. As in table, the data is already sorted out

#===================  1c  =========================
#------------Working with dataIMDB--------------
#First converting the character type language to factor(categorical type)
dataIMDB$Language = as.factor(dataIMDB$Language)
#Converting the categorical variable Language to Numeric type
dataIMDB$Language = as.numeric(dataIMDB$Language)

#------------working with dataIMDB2----------
dataIMDB2$Language = as.factor(dataIMDB2$Language)
dataIMDB2$Language = as.numeric(dataIMDB2$Language)

#==================  1e  ==========================
#------------Working with dataIMDB--------------
dataIMDB$squaredDiff_votes_rating = (dataIMDB$imdbVotes - dataIMDB$imdbRating)^2

#-----------Working with dataIMDB2------------
#converting character type to numberic for votes & rating
dataIMDB2$imdbRating = as.numeric(dataIMDB2$imdbRating)
dataIMDB2$imdbVotes = as.numeric(dataIMDB2$imdbVotes)
dataIMDB2$squaredDiff_votes_rating = (dataIMDB2$imdbVotes - dataIMDB2$imdbRating)^2


#-------------DONE--------------------#
#------Author: Aashit Singh----------#

