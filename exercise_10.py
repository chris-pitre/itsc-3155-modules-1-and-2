#Chris Pitre
#Intro to Python Exercises
#Exercise 10

stringToSplit = input("Enter a string: ")

#Unpacks the list to chars
#Strings are lists
#e.g. hello becomes ['h', 'e', 'l', 'l', 'o']
stringToSplit = [*stringToSplit]

#List Comprehension and List Slicing
#stringToSplit is split from i -> i+3 creating chunks of 3 chars
#e.g when i is 0, ['h', 'e', 'l', 'l', 'o'] becomes ['h', 'e', 'l']
#The range is the length of stringToSplit, but it increments in three, so i also increments in three
#e.g. after ['h', 'e', 'l'] is created, i becomes 3 giving us ['l', 'o']
#These lists beingn created are then put into the splitString list
#e.g. [['h', 'e', 'l'], ['l', 'o']]
splitString = [stringToSplit[i:i+3] for i in range(0, len(stringToSplit), 3)]

print(splitString)
