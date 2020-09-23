# همون فایل text رو بخون ولی نتیجه رو الان فقط داذی میگی بله پیدا شد، یا نه چنین چیزی پیدا نشد
# . بجای این خطوطی از خط ک پیدا شده رو در ی فایل تکست جدید بعنوان نتیجه بریز
#import necessary modules
import csv
import re




# asking user to enter wanted word
wantedword = input('please enter a word that you are looking for! like Ariana : ')    #String that you want to search

# first approach
with open('sample_tweets.csv', 'rt') as f:
     reader = csv.reader(f, delimiter=',') 
     for row in reader:
          for field in row:
              if field == wantedword:
                  print("is in file")


# # second approach
# a='like'     #String that you want to search
# with open("sample_tweets.csv") as f_obj:
#     reader = csv.reader(f_obj, delimiter=',')
#     for line in reader:      #Iterates through the rows of your csv
#         print(line)          #line here refers to a row in the csv
#         if a in line:      #If the string you want to search is in the row
#             print("String found in first row of csv")
#         break