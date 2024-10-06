#!/usr/bin/python
###############################################################
#Example 3: if-elif-else block
#           change the value of age to see which block executed
###############################################################

age = 5

if age <= 4:
    price = 0
elif age <= 18:
    price = 10
else:
    price = 20

print("Your Admission cost is $"+ str(price) + " .")
