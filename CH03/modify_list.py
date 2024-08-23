#!/usr/bin/python
################################################################
#Example to modify the content of list elements
################################################################
motorcycles = [ 'yamaha', 'honda', 'bajaj', 'suzuki' ]
print("--------------------------------------------------------")
print("motorcycle list brands")
print("--------------------------------------------------------")
print(motorcycles)
print("Replace the First element yamaha to ducati.")
motorcycles[0] = 'ducati'
print("--------------------------------------------------------")
print("After replacing the First element in motrocycles list  ")
print("--------------------------------------------------------")
print(motorcycles)
print("--------------------------------------------------------")
motorcycles[2] = 'hardley davidson'
print("--------------------------------------------------------")
print("After replacing the Third element in motrocycles list  ")
print("--------------------------------------------------------")
print(motorcycles)
#Adding an Element to motorcycles list.
#Appending happens to the end of the list
print("--------------------------------------------------------")
print("Appending enfiled to the motorcycles list ")
print("--------------------------------------------------------")
motorcycles.append('enfield')
print(motorcycles)
