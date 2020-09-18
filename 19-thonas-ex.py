import re

# opening sample_tweets file
f = open("sample_tweets 2.txt", "r")

# asking user to enter wanted word
txt = input('please enter a word! like Ariana: ')

# looking for the wanted word
x = re.search("^The.*Spain$", txt)

if x:
  print("YES! We have a match!")
  # Create a new file if it does not exist:
  f = open("result.txt", "w")
  f.write(txt)
  f.close() 

else:
  print("No match")



print('please get the result.txt file')

