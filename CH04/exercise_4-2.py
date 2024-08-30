#!/usr/bin/python 
#######################################################################
#4-2. Animals: Think of at least 3 different animals that have a common 
#     characterstic. Store the names of these animals in a list, and then
#     use a for loop to print out the name of each animal.
#==>  Modify program to print a statement about each animal, such as A dog would make a great pet.
#==>  Add a line at the end of your program starting what these animals have in common. You could
#     print a sentence such as Any of these animals would make a great pet!

pets = [ 'cat' , 'dog' , 'horse' ]
print("-----------------------------------------")
print("Below is pets list content::")
print("-----------------------------------------")

for pet in pets:
    print(pet.title())

print("---------------------------------------------------")
print("Modify program to print statement about each Animal")
print("---------------------------------------------------")

for pet in pets:
    print("A "+pet.title()+" would make a great pet.")

print("All the pets mentioned have in common they are all fast runners!!!")
