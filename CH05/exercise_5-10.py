#!/usr/bin/python
########################################################################################################################################
#5-10. Checking Usernames: Do the following to create a program that simulates how websites ensure that everyone has a unique name.
#==>   Make a list of 5 or more usernames called current_users.
#==>   Make another list of 5 usernames called new_users. Make sure 1 or 2 of the new usernames are also in the current_users list.
#==>   Loop through the new_users list to see if each new username has already been used. If it has, print a message that the person will
#      need to enter a new username. If a username has not been used, print a message saying that the username is available.
#==>   Make sure your comparison is case insensitive. If 'john' has been used, 'JOHN' should be accepted.

current_users = ['deeptha','varalakshmi','kamala','nagaraja','srini' ]
new_users     = [ 'kris','JOHN','srini','VARALAKSHMI','ted','Eric' ]

print("-------------------------------------")
print("current_users list :: ",current_users)
print("new_users list     :: ",new_users)
print("-------------------------------------")

if current_users and new_users:
    for new_user in new_users:
        if new_user.lower() in current_users:
            print("Need to enter new name, as "+new_user.title()+" already present in the current_users list")
        else:
            print("Welcome "+new_user.title()+" User to the Website !!!")

else:
    print("List is empty, ensure, current_users and new_users list at least has 1 element ")

