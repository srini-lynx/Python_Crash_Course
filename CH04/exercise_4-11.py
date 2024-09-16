#!/usr/bin/python
######################################
#4-11. My Pizzas, Your Pizzas: Start with your pizza program. Make a copy of 
#      the list of pizzas, and call it friend_pizzas. Then, do the following:
#      ==> Add a new pizza to the original list.
#      ==> Add a different pizza to the list friend_pizzas.
#      ==> Prove that you have two separate lists. Print the message,
#      My favourate pizzas are; and then use a for loop to print the second
#      list. Make sure each new pizza is stored in the appropriate list.
#
######################################

pizzas = ['veggie','chese','pepricon']
friend_pizzas = pizzas[:]
print("------------------------------------------------------------")
print("The elements in the list 'pizzas' :: ")
print("-------------------------------------------------------------")
print(pizzas)
print("-------------------------------------------------------------")
print("After copying the 'pizzas' to 'frined_pizzas' List")
print("'friend_pizzas' List has below Content::")
print(friend_pizzas)
print("-------------------------------------------------------------")
pizzas.append('mushroom')
print("Appending 'mushroom' pizza to the 'pizzas' List :: ")
print(pizzas)
friend_pizzas.append('bell-pepper')
print("Appending 'bell-pepper' pizza to the 'friend_pizzas' List ::")
print(friend_pizzas)
print("--------------------------------------------------------------")

print("-----------------------------")
print("PIZZA List has below Elements")
print("-----------------------------")

for pizza in pizzas:
  print(pizza.title())    
print("------------------------------------")
print("FRIEND PIZZA List has below Elements")
print("------------------------------------")

for fpizza in friend_pizzas:
    print(fpizza.title())
print("-------------------------------------")

