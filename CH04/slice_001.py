#!/usr/bin/python
###################################################
# Example for Copying List 
###################################################

orig_list = [ 'kamala','nagaraja','deeptha','varalakshmi' ]
print("-----------------------------------------------")
print("Please find orig_list content below")
print("-----------------------------------------------")
print(orig_list)
print("-----------------------------------------------")

update_list = orig_list[:]

print("--------------------------------------------------------------")
print("update_list copied from orig_list[:] and it's contents are ::")
print("--------------------------------------------------------------")
print(update_list)
print("--------------------------------------------------------------")

#To prove both orig_list and update_list are infact 2 different list
#Let's try to append some content to update_list and print both the lists

update_list.append('srinivasa')
print("------------------------------------------------------------------")
print("After appending 'srinivasa', the contents of update_list are ...")
print("------------------------------------------------------------------")
print(update_list)
print("------------------------------------------------------------------")
orig_list.append('lakshmi')
print("Let's find out the content of orig_list after appending 'lakshmi'..")
print(orig_list)
print("------------------------------------------------------------------")

#On the other hand, if we use = sign to assing the orig_list = update_list, then Python won't create 2 lists
#It just points update_list to same orig_list.

update_list = orig_list

print("After update_list = orig_list")
print("Contents of orig_list :: ")
print("---------------------------------------------------")
print(orig_list)
print("---------------------------------------------------")
print("Contents  of update_list :: ")
print(update_list)
print("---------------------------------------------------")

print("Append the Content of update_list with noone")
update_list.append('noone')
print("---------------------------------------------------")
print("Now the Contents of update_list ..")
print(update_list)
print("---------------------------------------------------")
print("Watch the Contents of orig_list, where we didn't do any appends")
print(orig_list)
print("---------------------------------------------------")
