#Chris Pitre
#Intro to Python Exercises
#Exercise 4

numFloats = int(input("Enter a number: "))
floatList = []

for i in range(numFloats):
    floatList.append(float(input("Enter number {}: ".format(i+1))))

print("List: {}".format(floatList))
average = sum(floatList)/len(floatList)

print("Average: {}".format(average))