#!/usr/bin/python
####################################################################
#Program: To generate a list of cubes from the range(1,11) and store in cube list
####################################################################
cubes = []

for value in range(1,11):
    cube = value * value * value
    cubes.append(cube)

print("------------------------------------------------------------------")
print("Below is the List of cubes within range(1,11)")
print("------------------------------------------------------------------")
print(cubes)
print("------------------------------------------------------------------")
