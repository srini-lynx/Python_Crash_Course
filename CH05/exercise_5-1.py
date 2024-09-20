#!/usr/bin/python
#####################################################
#5-1.Conditional Tests: 
#    Write a series of conditional tests.
#    Print a statement describing each test and your prediction for the results of each test.
######################################################

cars = ['toyota','audi','tesla','hundai','benz' ]
food = ['idly','dosai','vade','puri','pongal']
places = ['mandya','maduru','shivmoga','hubli','bengaluru']
temples = ['tirupathi','srirangapatna','beluru','halebidu','nanjanagudu']
languages = ['english','french','kannada','german','chiness']
#Predict 1

print("Is Car == 'tesla' ?")

PRD='tesla' in cars

if PRD:
    print("We predicted Right!!, Car is Tesla")
else:
    print("Sorry Wrong Prediction!!!")

#Predict 2
print("Is Food == 'puri' ?")

FD='puri' in food

if FD:
    print("We Predicted Right !!, Puri Available!!!")
else:
    print("Sorry, Puri outof Stock!!!")

#Predict 3
print("Is Place == 'bengalure' ?")
PL='bengaluru' in places

if PL:
    print("We Predicted Right !!, We love Bengaluru")
else:
    print("Sorry, We are not going to Bengalure")

#Predict 4
print("Is Temple == 'beluru' ?")
TM='beluru' in temples

if TM:
    print("We Predicted Right !!!, Beluru Temple in our list!!!")
else:
    print("Sorry, We are not going to Beluru Temple")


#Predict 5
print("Is Language == 'kannada' ?")
LG='kannada' in languages

if LG:
    print("We Predicted Right !!!, Kannada is the language you love !!!")
else:
    print("Sorry, the Language you choose not available right now")


#Predict 6
VH= 'bently' in cars

print("Is Car == 'bently'")

if VH:
    print("Yes it's right Bently Car!!!")
else:
    print("We don't have Bently Car right now !!!")

#Predict 7
FD='karabath' in food

print("Is Food == 'karabath' ?")

if FD:
    print("Karabath Surprisingly available !!!")
else:
    print("We don't have 'karabath' at this moment !!!")

#Predict 8
PL='mumbai' in places

print("Is Place == 'mumbai' ?")

if PL:
    print("Mumbai Place we can visit")
else:
    print("We don't have any schedule for 'mumbai' !!!")

#Predict 9
TM='kashi' in temples

print("Is Temple == 'kashi' ?")

if TM:
    print("Yes Kashi is scheduled this year ")
else:
    print("We don't have scheduled tour to 'kashi' this year !!!")

#Predict 10
LG='tamil' in languages

print("Is Language == 'Tamil' ?")

if LG:
    print("Ah.. It's not the language of my choice...!!!")
else:
    print("hmm, We never team 'Tamil' over hear!!!!")

