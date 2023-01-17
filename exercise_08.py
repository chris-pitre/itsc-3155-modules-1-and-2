#Chris Pitre
#Intro to Python Exercises
#Exercise 8

intList = []

for i in range(10):
    intList.append(int(input("Enter number {}: ".format(i+1))))

print("Original List: {}".format(intList))

#List Comprehension
#Creates a list singleNum from intList where each element of intList only appears once
singleNum = [i for i in intList if intList.count(i) == 1]

print("Nums that appear once: {}".format(singleNum))