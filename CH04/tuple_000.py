#!/usr/bin/python
###################################################
#Some times we will want to create a list of items that cannot change.
#A Tuple allows you to do just that. Python refers to values that cannot
#change as 'immutable', and an immutable list is called as a tuple.
#A Tuple looks just like a list except we use parenteses instead of
#Square brackets. Once we define a tuple, we can access individual
#elements by using each item's index, just as we would for a list.
###################################################
#An Ex: rectangle size will always be of certain size, and it can be a tuple.

dimenstion = (100,50)

print("Dimension of the rectangle are ::")
for side in dimenstion:
    print("Side of Rectangle in CM's :: ",side)

#############################################
###Try to Modify tuple Value, Python errors::
##############################################

#dimenstion[0] = 200

#print("---------------------------------------")
#print("Modified dimesion values :: ",dimenstion)
#print("---------------------------------------")

#TypeError: 'tuple' object does not support item assignment

###############################################

print("Although tuple modifications are not allowed, Assignment is allowed")

dimenstion = (500,50,100)


print("----------------------------------------------------------------------")
print("After dimenstions = (500,50,100), the contents of dimenstions tuple are ::")
print("----------------------------------------------------------------------")
for side in dimenstion:
    print("Updated Dimension after assignment :: ",side)
print("----------------------------------------------------------------------")

