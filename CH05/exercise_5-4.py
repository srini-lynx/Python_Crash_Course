#!/usr/bin/python
#############################################################################################
#Example:5-4. Alien Colors#2: Choose a color for an alien as in 5-3, and write an if-else chain
#==>  If the alien's color is green, print a statement that the player just earned 5 points for
#     shooting the alien.
#==>  If the alien's color isn't green, print a statement that the player just earned 10 points.
#==>  Write one version of this program that runs if block and another that runs the else block.
#############################################################################################

#V1

alien_color = 'green'
print("-------------")
print("Version 1 :: ")
print("-------------")
if alien_color == 'green':
    print("Player just earned 5 points for shooting the alien")
    print("----------------------------------------------------------")
else:
    print("Player just earned 10 points")

print("----------------------------------------------------------")

alien_color= 'yellow'
print("------------")
print("Version 2 :: ")
print("------------")
if alien_color == 'green':
    print("Player just earned 5 points")
else:
    print("----------------------------------------------------------")
    print("Player just earned 10 points !!!")
    print("----------------------------------------------------------")
