#!/usr/bin/python
##################################################################################################################################################
#5-8. Hello Admin: Make a list of 5 or more usernames, including the name 'admin'. Imagine you are writing code that will print a greeting to each
#     user after they log into a website. Loop through the list, and print a greeting to each user:
# ==> If the username is 'admin', print a special greeting, such as Hello Admin, would you like Status Report ?
# ==> Otherwise, print a generic greeting, such as Hello Eric, thank you for logging in again!!!

users = ['deeptha','lakshmi''kamala','admin','nagaraja']

for user in users:
    if user == 'admin':
        print("Hello Admin, Would you like to view the System Report ?")
    else:
        print("Hello "+user.title()+" Welcome back to the Website !!!")

