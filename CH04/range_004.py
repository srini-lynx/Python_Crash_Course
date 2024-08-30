#!/usr/bin/python
###################################################################
#Program using range() to create a list of squares

squares = []

for value in range(1,11):
    square = value ** 2
    squares.append(square)

print("----------------------------------------------------------------------")
print("Below is the list of squares generated from range (1,11) i.e., 1 to 10")
print("----------------------------------------------------------------------")
print(squares)
print("----------------------------------------------------------------------")


