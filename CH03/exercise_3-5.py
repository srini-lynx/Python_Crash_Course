#!/usr/bin/python
######################################################################################
#3-5.You just heard that one of your guests can't make the dinner, so you need to send
#out a new set of invitations. You'll have to think of someone else to invite.
#=>Start with prev program. Add a print statement at the end of your program starting 
#the name of the guest who can't make it.
#=> Modify your list, replacing the name of the guest who can't make it with the name
#of the new person you are inviting.
#=>Print a second set of invtitation messages, one for each person who is still in 
#your list.
######################################################################################
guests = ['Lakshmi Devi', 'Nagaraja','Varalakshmi']

print("Hello "+guests[0]+ " Your invited for tonights dinner, Please be available!!!")
print("Hello "+guests[1]+ " Your invited for tonights dinner, Please don't forget!!!")
print("Hello "+guests[2]+ " Your invited for tonights dinner, Please get yourself ready!!!")
print("Ah!!! Just got update from "+guests[2]+" unable to attend dinner due to personal reason")
not_attending = guests.pop()
print("Dear "+not_attending+", We miss you this time!!! ")
print("Appending Deeptha to guests list::")
print("Now the guests list contains")
guests.append('Deeptha')
print("------------------------------------------------------------------")
print(guests)
print("-------------------------------------------------------------------")
print("Updated Invitation List")
print("Hey ! "+guests[0]+" Please accept our invitation for the Dinner tonight !!!")
print("Hey ! "+guests[1]+" Please accept our invitation for the Dinner tonight !!!")
print("Hey, ! "+guests[2]+" Please accept our invitation for the Dinner tonight!!!")
