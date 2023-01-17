#Chris Pitre
#Intro to Python Exercises
#Exercise 3

cubeInt = int(input("Enter an integer greater than 1: "))

for i in range(cubeInt+1):
    #{} gets filled in by format() method
    print("The cube of {} is {}".format(i, i**3))