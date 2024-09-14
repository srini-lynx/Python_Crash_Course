#!/usr/bin/python
#######################################################################
#Slicing List Example::
#in order to slice 3 elements [0:3]
#######################################################################

players = ['charles', 'babagge','denis','ritche','pike','kerneghan','bob','walace','jack' ]

print("List players contains ::")
print(players)
print("players[0:3] will have below players list")
print(players[0:3])

#subset in players list from element 1 to 4
print("Players from 1 to 4")
print(players[1:4])
#Ommit the begining of list in slicing always starts the slicing from begining
print("Players from [:5], from 1st Eelement to 4th Element of the list")
print(players[:5])
print("Players from [2:], from 2nd Element to end of list")
print(players[2:])
print("Players from [-3:],  last 3 element from end of list")
print(players[-3:])
##Print the list of items through slicing and using for loop to individual element
print("---------------------------------------------------------------------")
print("Hear are the first 3 players from the list of plyaers from the team!!!")
for player in players[:3]:
    print("Selected Player :: ",player.title())
print("---------------------------------------------------------------------")


