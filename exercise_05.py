#Chris Pitre
#Intro to Python Exercises
#Exercise 5

firstList = []
secondList = []

for i in range(5):
    firstList.append(int(input("Enter a number for the first list: ")))

for i in range(5):
    secondList.append(int(input("Enter a number for the second list: ")))

print("First List: {}".format(firstList))
print("Second List: {}".format(secondList))

#Creates a set of the first list then finds any intersections with the second list, then turns the set into a list
#e.g. [1, 2, 3, 3, 4] becomes {1, 2, 3, 4} which intersects with [1, 3, 6, 7] giving {1, 3} which is turned into [1, 3]
commonList = list(set(firstList).intersection(secondList))

print("Common List: {}".format(commonList))