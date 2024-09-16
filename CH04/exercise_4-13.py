#!/usr/bin/python
#############################################
#4-13.Buffet: A buffet-style resturant offers only 5 basic foods.
#     Think of 5 simple foods, and store them in tuple.
#   ==> Use a for loop to print each food the resturant offers.
#   ==> Try to modify one of the items, and make sure that Python
#       rejects the change.
#   ==> The resturant changes it's menu, replacing 2 of the items with
#       different foods. Add a block of code that rewrites the tuple, 
#       and then use a for loop to print each of the items on the 
#       revised menu.
###############################################
foods = ('anna sambar','millet bisibelebath','upittu','kesari bath','masala dosai','iddly')

print("------------------------")
print("Deeptha's Resturant Menu")
print("------------------------")
for item in foods:
    print(item.title())
print("------------------------")

########################################

#Below code will error out so commented.
#foods[0] = 'mudde'
#print("anna sambar replaced by :: ",foods[0])
#TypeError: 'tuple' object does not support item assignment

########################################

#We can assign the value to tuple, there by modifying which otherwise not possible
#Update the 'upittu' with 'kara bath'

foods = ('anna sambar','millet bisibelebath','kara bath', 'masala dosai','iddly')

print("----------------------------")
print("Deeptha's Menu Update")
print("----------------------------")
for item in foods:
    print(item.title())
print("----------------------------")
