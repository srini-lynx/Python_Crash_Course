#!/usr/bin/python
############################################################################################
#Example 5: Use only if statements if multiple block of code needs to execute, unlike elif
#           which executes only 1 block of code rest will be ignored.
#           in this example if-elif block will not work properly as it will only execute
#           1 block and rest of the block will get ignored if the previous one evaluates to 
#           true.
############################################################################################

toppings = ['mushroom','peppricon','extra cheese']

if 'extra cheese' in toppings:
    print("Adding extra cheese, to pizza")
if 'peppricon' in toppings:
    print("Adding extra peppricon, to pizza")
if 'mushroom' in toppings:
    print("Adding mushroom to pizza")
