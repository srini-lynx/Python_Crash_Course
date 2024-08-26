#!/usr/bin/python

#3.7 Shrinking Guest List:
#The new dinner table won't arrive on time, and you have space only for 2 guests.
#==> Start with your program from PREV 3.6 program, Add a new line that prints message
#    saying that you can invite only 2 people for dinner.
#==> Use pop() to remove guests from your list one at a time, until only 2 names remain in list.
#    Each time you pop a name from your list, print a message to that person letting them know
#    you're sorry you can't invite them to dinner.
#==> Print a message to each of the two people still on your list, letting them know they're still
#    invited.
#==> Use del to remove the last two names from your list, so you have an empty list. Print your list
#    to make sure you actually have an empty list at the end of your program.

#List Guests

guests = ['lakshmi devi','deeptha srinivasa', 'nagaraja', 'srinivasa', 'varalakshmi','annapurna']

print("----------------------------------------------------------------------------")
print("Invited Guests lists are ::")
print("----------------------------------------------------------------------------")
print(guests)
print("----------------------------------------------------------------------------")
print("Update about the Up-Coming Party")
print("----------------------------------------------------------------------------")
print("We are sorry to inform you that, following guests invite withdrawn due to dinner table issue")
print("----------------------------------------------------------------------")
last = guests.pop()
print("Hi ",last.title()+" We regret to inform you that you're invitation remains void")
last1 = guests.pop()
print("Hi ",last1.title()+" We regret to inform you that you're invitation remains void")
last2 = guests.pop()
print("Hi ",last2.title()+" We regret to inform you that you're invitation remains void")
last3 = guests.pop()
print("Hi ", last3.title()+" We regret to inform you that you're invitation remains void")
print("----------------------------------------------------------------------")
print("Current in the list of Invites ::")
print(guests[0].title())
print(guests[1].title())
print("----------------------------------------------------------------------")
print("Removing the elements of the guests list, as the invitation sent ")
del guests[0]
print("After removing the first element of the list, list content")
print(guests)
print("After removing the second element,(now it's the first element) of the list, list content")
del guests[0]
print(guests)
print("----------------------------------------------------------------------")
print("All elements removed from the guests list, and it's empty not")
print(guests)
print("----------------------------------------------------------------------")
