#!/usr/bin/python
###############################################################################################################################
#5-9: Add an if test to make sure the list is not empty.
#==>  If the list is empty, print the message, We need to find some users!
#==>  Remove all of the usernames from the list, and make sure the correct message printed out.
###############################################################################################################################
users = []
#users = [ 'deeptha','admin','kamala','nagaraja','lakshmi']

if users:
    for user in users:
        if user == 'admin':
            print("Hello "+user.title()+" Would you like to check System Report ?")
        else:
            print("Hello "+user.title()+" Welcome back to the website !!!")
else:
    print("No users found!!! List is empty")
