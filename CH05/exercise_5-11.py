#!/usr/bin/python
###########################################################################################################################################
#5-11. Ordinal Numbers: It indicates their position in a list, such as 1st, 2nd, 3rd , 4th etc. Most end up with th other than 1 2 and 3
#==>   Store the numbers, from 1 to 9 in a List.
#==>   Loop through the List.
#==>   Use an if-elif-else chain inside the loop to print the proper ordinal ending for each number. Your output should read 
#      1st 2nd 3rd 4th 5th 6th 7th 8th and 9th, and each output should be in a separate line.
###########################################################################################################################################

numbers = [1,2,3,4,5,6,7,8,9]
print("----------")
print("Numbers ::")
print("----------")
if numbers:
    for number in numbers:
        if number == 1:
            print("1st")
        elif number == 2:
            print("2nd")
        elif number == 3:
            print("3rd")
        else:
            print(str(number)+"th")

print("----------")
