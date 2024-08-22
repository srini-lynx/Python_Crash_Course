#!/usr/bin/python
########################################################################################
#3-2. Greetings: Start with the list you used in Exercise 3-1, but instead of just
#printing each person’s name, print a message to them. The text of each mes-
#sage should be the same, but each message should be personalized with the
#person’s name and also with title() method.
########################################################################################
friends_names = [ 'nagaraj','asha','kudva','shobha' ]
print("------------------------------------------------------------------------------------")
print("List friends_names contains following names, messages are added for greeting purpose")
print("------------------------------------------------------------------------------------")
print("Hi "+friends_names[0].title()+" , how is your day?")
print("Hey "+friends_names[1].title()+", how are you doing today?")
print("Hi! "+friends_names[2].title()+", is everything good from your end?")
print("Hell "+friends_names[3].title()+", i hope you are doing fine!!!")
print("------------------------------------------------------------------------------------")
