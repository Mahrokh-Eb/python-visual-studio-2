# همون فایل text رو بخون ولی نتیجه رو الان فقط داذی میگی بله پیدا شد، یا نه چنین چیزی پیدا نشد
# . بجای این خطوطی از خط ک پیدا شده رو در ی فایل تکست جدید بعنوان نتیجه بریز
#import necessary modules
import csv
import re

# asking user to enter wanted word
#wantedWord = input('please enter a word that you are looking for! like Ariana : ')
wantedWord = 'like'

# opening sample_tweets file
with open('sample_tweets.csv','rt')as f:
      data = csv.reader(f)
      for row in data:
          print(row)


# looking for the wanted word
x = re.search( wantedWord, row)
print(x)


# if x:
#   print("YES! We have a match!")
#   # Create a new file if it does not exist:
#   f = open("result.txt", "w") # w will overwrite on existing file
#   f.write('yes we have a match')
#   f.close() 

# else:
#   print("No match")
#   f = open("result.txt", "w") 
#   f.write('Unfortunately, I see no match')
#   f.close() 
