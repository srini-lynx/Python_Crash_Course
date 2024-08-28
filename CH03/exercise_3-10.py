#!/usr/bin/python
################################################################################################
#3-10. Every Function: Think of something you could store in a list. For example, you could make
#      a list of mountains, rivers, countries, cities, languages, or anything else you'd like.
#      Write a program that creates a list containing these items and then use each function 
#      introduced in this chapter at least once.
################################################################################################

districts = [ 'bengaluru', 'shivmoga', 'tumkur', 'chikkabalapura', 'sirsi', 'udupi' , 'dakshina kannada', 'agumbey' ]
print("---------------------------------------------------------------------------------------------------")
print("districts list content::")
print(districts)
print("---------------------------------------------------------------------------------------------------")
sorted_districts = sorted(districts)
print("sorted(districts) ::")
print(sorted_districts)
print("--------------------------------------------------------------------------------------------------")
descend_districts = sorted(districts,reverse=True)
print("sorted(districts,reverse=True)")
print(descend_districts)
print("--------------------------------------------------------------------------------------------------")
print("districts.reverse()")
districts.reverse()
print(districts)
print("--------------------------------------------------------------------------------------------------")
print("Again if we use districts.reverse() will bring back previous order...")
districts.reverse()
print(districts)
print("--------------------------------------------------------------------------------------------------")
print("districts.sort()")
districts.sort()
print(districts)
print("--------------------------------------------------------------------------------------------------")
districts.sort(reverse=True)
print("districts.sort(reverse=True)")
print(districts)
print("--------------------------------------------------------------------------------------------------")
print("The number of elements of the list districts::")
num_of_districts = len(districts)
print(num_of_districts)
print("--------------------------------------------------------------------------------------------------")
