#!/usr/bin/python
###############################################################################################################
# 3-8: Seeing the world: Think of at least 5 places in the world you'd like to visit.
# => Store the location in a list. Make sure the list is not in alphabetical order.
# => Print your list in it's original order. Don't worry about printing the list neatly,
#    Just print it as a raw Python list.
# => Use sorted() to print your list in alphabetical order wihtout modifying the actual list.
# => Show that your list is still in it's original order by printing it.
# => Use sorted() to print your list in reverse alphabetical order withought changing the order
#    of the original list.
# => Use reverse() to change the order of your list. Print the list to show that it's order has
#    has changed.
# => Use reverse() to change the order of your list again. Print the list to show it's back to 
#    it's original order.
# => Use sort to change your list so it's stored in alphabetical order. Print the list to show
#    it's back to it's original order.
# => Use sort() to change your list so it's stored in alphabetical order. Print the list to show
#    that it's order has been changed.
# => Use sort() to change your list so it's stored in reverse alphabetical order.
#    Print the list to show that it's order has changed.
###############################################################################################################

places = [ 'india', 'usa', 'france', 'switzerland', 'poland'  ]

print("------------------------------------------------------------------------------------------------")
print("places list content ::")
print("------------------------------------------------------------------------------------------------")
print(places)
orig_places = sorted(places)
print("orig_places list has")
print(orig_places)
print("------------------------------------------------------------------------------------------------")
print("------------------------------------------------------------------------------------------------")
print("Original places sotred and stored in  orig_places list in alphabetical order")
print(orig_places)
print("------------------------------------------------------------------------------------------------")
print("------------------------------------------------------------------------------------------------")
orig_reverse = sorted(places,reverse=True)
print("Original places sorted in reverse order and stored in orig_reverse list content ...")
print(orig_reverse)
print("------------------------------------------------------------------------------------------------")
print("------------------------------------------------------------------------------------------------")
print("Places in Alphabetical Order, without modifying the Original content of list places")
print("------------------------------------------------------------------------------------------------")
print(sorted(places))
print("------------------------------------------------------------------------------------------------")
print("Re-check the Content of places list to ensure the orders are not changed..")
print(places)
print("------------------------------------------------------------------------------------------------")
print("Now printing the list in reverse alphabetical order, without modifying the places list")
print(sorted(places,reverse=True))
print("------------------------------------------------------------------------------------------------")
print("Now printing the Content of list places, to ensure it's not modified")
print("------------------------------------------------------------------------------------------------")
print(places)
print("------------------------------------------------------------------------------------------------")
print("use reverse(), to permanently reverse the places list in reverse order")
print("------------------------------------------------------------------------------------------------")
places.reverse()
print(places)
#print(places.reverse())
print("------------------------------------------------------------------------------------------------")
print("Now the list places is permanently reversed")
print("------------------------------------------------------------------------------------------------")
print(places)
print("------------------------------------------------------------------------------------------------")
print("It should be quick fix to reverse again to get back the original places list !!!")
print("------------------------------------------------------------------------------------------------")
places.reverse()
print(places)

print("------------------------------------------------------------------------------------------------")
print("Use sort() to permanently change the places list in alphabetical order")


places.sort()
print(places)
print("-----------------------------------------------------------------------------------------------")
print("Use sort(reverse=True) to permanently change the places list in reverse alphabetical order")
print("-----------------------------------------------------------------------------------------------")
places.sort(reverse=True)
print(places)





print("**************************E.N.D   O.F.  P.R.O.G.R.A.M******************************************")


