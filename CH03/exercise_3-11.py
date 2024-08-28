#!/usr/bin/python
##########################################################################################################
#3-11. Intentional Error: if you haven't received an index error in one of your program yet, try to make 
#      one happen. Change an index in one of your programs to produce an index error. Make sure you correct 
#      the error before closing the program.
##########################################################################################################

places = [ 'india', 'usa', 'france', 'japan', 'russia', 'ukrain', 'newzeland', 'australia' ]

print("The Contents of places list are :: ")
print(places[0].title())
print(places[1].title())
print(places[2].title())
print(places[3].title())
print(places[4].title())
print(places[5].title())
print(places[6].title())
print(places[7].title())
print("Next item will fail as the index is out of range....")
print("print(places[8].title())")
print("We can always use places[-1].title(), which always represents the last item in the list")
print("One Catch is that while using index [-1], ensure that list is not empty otherwise again index error we will get...")
print(places[-1].title())
