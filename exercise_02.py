#Chris Pitre
#Intro to Python Exercises
#Exercise 2

firstString = input("Enter a string: ")
secondString = input("Enter another string: ")

#Prints True or False whether or not firstString is in secondString
#or if secondString is in firstString
#e.g. car in carpet or carpet in car -> True or False -> True
#e.g. carpet in car or car in carpet -> False or True -> True
print(firstString in secondString or secondString in firstString)