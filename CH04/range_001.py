#!/usr/bin/python
##################################################
#Example : range() to make a list of numbers.
#          When we wrap list() around a call to range(),
#          the output will be a list of numbers.
##################################################

numbers = list( range(1,21))

print("----------------------------------------------------------")
print("Below is the list of numbers generated with rang(1,21)")
print("----------------------------------------------------------")

for num in numbers:
    print("Generated number :: ",num)

print("------------------END OF LIST-----------------------------")

