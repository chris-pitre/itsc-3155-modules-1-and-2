#Chris Pitre
#Intro to Python Exercises
#Exercise 6

#Creates a 5x5 matrix
# 0 0 0 0 0
# 0 0 0 0 0
# 0 0 0 0 0
# 0 0 0 0 0
# 0 0 0 0 0
matrix = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

m = int(input("Enter a row num from 1 to 5: ")) - 1
n = int(input("Enter a col num from 1 to 5: ")) - 1

#Uses the m and n inputs as row and columns in the matrix and changes the value to 1
# (2, 4) creates this
# 0 0 0 0 0
# 0 0 0 1 0
# 0 0 0 0 0
# 0 0 0 0 0
# 0 0 0 0 0
matrix[m][n] = 1

#For each element in matrix (e.g. [0, 0, 0, 0, 0]) it turns it into an equivalent string
#It then joins it together with a space (e.g. 0 0 0 0 0)
#Does this for each row
for i in matrix:
    print(" ".join(map(str, i)))
