#Chris Pitre
#Intro to Python Exercises
#Exercise 9

stringList = []

for i in range(5):
    stringList.append(input("Enter a word: "))

print("Words: {}".format(stringList))

print("One String: " + " ".join(stringList))