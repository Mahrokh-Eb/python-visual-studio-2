import re

# opening sample_tweets file
f = open("sample_tweets 2.txt", "r")
# print(f.read())

# asking user to enter wanted word
wantedWord = input('please enter a word that you are looking for! like Ariana : ')

# looking for the wanted word
x = re.search( wantedWord, f.read())
print(x)

if x:
  print("YES! We have a match!")
  # Create a new file if it does not exist:
  f = open("result.txt", "w") # w will overwrite on existing file
  f.write('yes we have a match')
  f.close() 

else:
  print("No match")
  f = open("result.txt", "w") 
  f.write('Unfortunately, I see no match')
  f.close() 

# print('please get the result.txt file')

