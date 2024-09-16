#!/usr/bin/python
###################################
#4-10. Slices: Using any of the earlier program, add several lines to the 
#      end of the program that do the following:
#      ==> Print the msg, The first 3 items in the list are: Then use a slice
#      to print the first three items from that program's list.
#      ==> Print the msg, 3 items from the middle of the list are: Use a slice
#      to print three items from the middle of the list.
#      ==> Print the message, The last three items in the list are: Use a slice
#      to print three items from the middle of the list.
#
####################################
pets = ['cat','dog','fish','parrot','hosrse','bunny','eagle','pig','snake','snail' ]

print("-----------------------------------------------")
print("The Contents of list 'pets' are ::")
print("-----------------------------------------------")
print(pets)
print("-----------------------------------------------")
print("The First 3 elements of the 'pets' list are ::")
print("-----------------------------------------------")
print(pets[:3])
print("-----------------------------------------------")
count=len(pets)
print("Number of pets in 'pets' list ::")
print(count)
print("-----------------------------------------------")
middle=int(count/2)
nxt=middle+2
print("Middle element can be :: ")
print(middle)
print("------------------------------------------------")
print("The 3 elements in list 'pets' from middle are::")
print(pets[middle-1:nxt])
print("------------------------------------------------")
print("The Last 3 elements from list 'pets' are ::")
print(pets[-3:])
print("------------------------------------------------")
