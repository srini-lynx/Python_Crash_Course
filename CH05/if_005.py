#!/usr/bin/python
#####################################################################################################
#Example-5: if-elif block
#           The else block is catch all statement. It matches any condition that wasn't matched by a 
#           specific if or  elif test, and that sometime include invalid or even malicious data.
#           If we have a specific final condition to be tested for, consider using elif block and 
#           omit the else block. As a result, we will gain extra confidence that our code will run
#           only under the correct condition.
#####################################################################################################

age = 65

if age <= 4:
    price = 0
elif age <= 18:
    price = 10
elif age <= 64:
    price = 20
elif age > 64:
    price = 5

print("The Admission Fees is $"+str(price)+" .")
