#!/usr/bin/python
#############################################################################
#4-9. Cubes Comprehension:
#     Use a list comprehension to generate a list of the first 10 cubes. 
##############################################################################

cubes = [cube ** 3 for cube in range(1,11) ]

print("--------------------------------------------------------------------------")
print("cubes list from range (1,11) using list comphresion technique::")
print(cubes)
print("--------------------------------------------------------------------------")
