#!/usr/bin/python
#############################################################################################
#5-5. Alien Color#3: Turn your if-else chain from 5-4 into if-elif-else chain.
#==> If alien green, print a message that the player earned 5 points.
#==> If alien yellow, print a message that the player earned 10 points.
#==> If alien red, print a message that the player earned 15 points.
#==> Write 3 version of program each printing corresponding alien color
#    V1 alian_color= 'green', V2 alian_color = 'yellow' and V3 alian_color = 'red'
#Caviate:: for V3 any color or any change in alien_color variable value  still we get 15 point !!!!
#          due to the fact that else will account for all the values other than the condition if !!!!
#          which can be mitigated by using the elif instead of else !!!!
#############################################################################################
alien_color = 'white'

if alien_color == 'green':
    print("Player just earned  5 points")
elif alien_color == 'yellow':
    print("Player just earned 10 points")
else:
    print("Player just earned 15 points")
