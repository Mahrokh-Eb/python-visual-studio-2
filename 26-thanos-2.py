#Check whether string is in CSV (sample_tweets.csv) - sample_tweets

#import necessary modules
import csv
import re

# # asking user to enter wanted word
# wantedword = input('please enter a word that you are looking for! like Ariana : ')    #String that you want to search

# # first approach
# with open('sample_tweets.csv', 'rt') as f:
#      reader = csv.reader(f, delimiter=',') 
#      for row in reader:
#           for field in row:
#               if field == wantedword:
#                   print("is in file")


# second approach
# a='bbb'     #String that you want to search
# with open("sample_tweets.csv") as f_obj:
#     reader = csv.reader(f_obj, delimiter=',')
#     for line in reader:      #Iterates through the rows of your csv
#         print(line)          #line here refers to a row in the csv
#         if a in line:      #If the string you want to search is in the row
#             print("String found in first row of csv")
#         break


# # third approach - successfull, read from a csv file and make a txt file and write on it
# #Open file with "w"(write), the file will create automatically.
# file = open("new.txt", "w")
# #Open CSV file to read CSV, note: reading and write file should be under "with"
# with open('sample_tweets.csv') as csvFile:
#     #Read CSV
#     readCsv = csv.reader(csvFile)
#     for row in readCsv:
#         #Get Values and manupilate in the file.write
#         Id = row[0]
#         Id1 = row[1]
#         #Write CSV you need format it to string if the value is an int
#         file.write("UPDATE Schema.TableName SET Column1="+str(Id1)+" where Column2="+str(Id)+";\n")
# #You Must Close the FIle after writing it.
# file.close()




# # opening the CSV file 
# with open('sample_tweets.csv', mode ='r')as file: 
    
#   # reading the CSV file 
#   csvFile = csv.reader(file)  
# #   # displaying the contents of the CSV file 
# #   for lines in csvFile: 
# #         print(lines) 
  
# # # search for a word in cvs file with panda library
# import pandas 
# # reading the CSV file 
# csvFile = pandas.read_csv('sample_tweets.csv')  
# # displaying the contents of the CSV file 
# #print(csvFile) 

#####################################################################

username = input('Enter:  ')
file = open("new.txt", "w")
with open('sample_tweets.csv', 'rt') as f:
     reader = csv.reader(f, delimiter=',') # good point by @paco
     for row in reader:
          for field in row:
              if field == username:
                  print( "is in file")
                  file.write(row)
#You Must Close the FIle after writing it.
                  file.close()

#####################################################################
# username = 'goli'
# is_in_file = False
# with open('sample_tweets.csv', 'rb') as csvfile:
#     my_content = csv.reader(csvfile, delimiter=',')
#     for row in my_content:
#         if username in row:
#             is_in_file = True
# print ('is_in_file')
####################################################################
# # third approach - successfull, read from a csv file and make a txt file and write on it
# #Open file with "w"(write), the file will create automatically.
# file = open("new.txt", "w")
# #asking user to put favorite word
# wantedword = input('Enter the word you are Looking for: ')
# #Open CSV file to read CSV, note: reading and write file should be under "with"
# with open('sample_tweets.csv') as csvFile:
#     #Read CSV
#     readCsv = csv.reader(csvFile)
#     for row in readCsv:
#         #Get Values and manupilate in the file.write
#         Id = row[0]
#         Id1 = row[1]
#         #Write CSV you need format it to string if the value is an int
#         file.write("UPDATE Schema.TableName SET Column1="+str(Id1)+" where Column2="+str(Id)+";\n")
# #You Must Close the FIle after writing it.
# file.close()