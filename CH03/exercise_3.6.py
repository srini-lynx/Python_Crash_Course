#!/usr/bin/python
#3-6. More Guests: You just found a bigger dinner table, so now more space is available. Think of 
#three more guests to invite to dinner.
#==> Start your program informing people that you found a bigger dinner table.
#==> Use insert() to add one new guest to the beginning of your list.
#==> Use insert() to add one new guest to the middle of your list.
#==> Use append() to add one new guest to the end of your list.
#==> Print a new set of invitation messages, one for each person in your list.
guests = ['lakshmi devi', 'nagaraja', 'srinivasa', 'varalakshmi' ]
print("---------------------------------------------------------------")
print("Please find the List of Invites to the Upcoming Party !!!")
print("---------------------------------------------------------------")
print("Hi ",guests[0].title()+" you'r invivited to the party!!!")
print("Hi ",guests[1].title()+" you'r invited to the party!!!")
print("Hi ",guests[2].title()+" you'r invited to the party!!!")
print("Hi ",guests[3].title()+" you'r invited to the party!!!")
print("---------------------------------------------------------------")
print("Updated Status about the Party...")
print("Good news we got Bigger Table, How cool is that, slots are open for 3 more guests...")
guests.insert(0,'kammala nagaraja')
guests.insert(2,'annapurnamma')
guests.append('deeptha')
print("---------------------------------------------------------------------------")
print("Now the Updated Guests are ::")
print("---------------------------------------------------------------------------")
print(guests)
print("---------------------------------------------------------------------------")
print("Hello ", guests[0].title()+" Please be available for the Party !!!")
print("Hello ", guests[1].title()+" Please be available for the Party !!!")
print("Hello ", guests[2].title()+" Please be available for the Party !!!")
print("Hello ", guests[3].title()+" Please be available for the Party !!!")
print("Hello ", guests[4].title()+" Please be available for the Party !!!")
print("Hello ", guests[5].title()+" Please be available for the Party !!!")
print("Hello ", guests[6].title()+" Please be available for the Party !!!")
print("---------------------------------------------------------------------------")
