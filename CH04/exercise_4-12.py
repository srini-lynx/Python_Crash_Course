#!/usr/bin/python
##################################
#4-12. More Loops: All versions of foods.py in this section have avoided
#      using for loops when printing to save space. Choose a version of
#      foods.py, and write two for loops to print each list of foods.
##################################
my_foods = ['pizza','falafel','carrot cake','ice cream','mudde','anna sambar']

friend_foods = ['masala dosa','idly','vade','pizza','falafel','cake']

print("---------------------------------------")
print("My Foods are ::")
print("---------------------------------------")
for mfood in my_foods:
    print("Favaourate Food :: ",mfood.title())

print("---------------------------------------")
print("---------------------------------------")
for ffood in friend_foods:
    print("Friends Food :: ",ffood.title())

print("---------------------------------------")


