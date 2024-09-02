#!/usr/bin/python
############################################################################
#4.8 Cubes: A number raised to the 3rd power is called a cube. For ex:,
#    the cube of 2 is written as 2 ** 3 in Python. Make a list of the first 10 cubes
#    (that is, the cube of each integer from 1 through 10), and use a for loop to print
#    out the value of each cube.
#############################################################################

cubes = []
for cube in range(1,11):
    cube = cube ** 3
    cubes.append(cube)

print("---------------------------------------------------------------")
print("List cubes from range(1,11)")
print("---------------------------------------------------------------")
print(cubes)
print("---------------------------------------------------------------")
