#!/usr/bin/python
##################################
#5-2.More Conditional Tests:
#    We don't have to limit the number of tests you create to 10.
#    if we want to try more comparisions, write more tests and add
#    them to conditional_test.py. Have at least one True and one 
#    False result for each of the following:
# ==> Tests for equality and inequality with strings.
# ==> Tests using the lower() function.
# ==> Numerical tests involiving equality, and inequality, greater than and 
# ==> less than, greater than or equal to, and less than or equal to
# ==> Tests using the and keyword and the or keyword.
# ==> Test whether an item is in a list.
# ==> Test whether an item is not in a list.
##################################

cars = ['tesla','bmw','lucid','hundai','toyota','']

car = 'bmw'

if car == 'bmw':
    print("Car is indeed BMW")
else:
    print("Wrong Car !!!")


car = 'lucid'

if car != 'lucid':
    print("CAR is NOT LUCID")
else:
    print("CAR is indeed LUCID")


car = 'HUNDAI'

if car.lower() == 'hundai':
    print("car is hundai")
else:
    print("car is not HUNDAI")

car = 'toyota'

if car.upper() == 'TOYOTA':
    print("CAR is TOYOTA")
else:
    print("Car is not toyota")

age = 27

if age >= 30:
    print("Age value is less than or equal to 30:: and Value is ::  ",age)
else:
    print("Age Value is :: ", age )

ans = 42

if ans != 20:
    print("That's not the correct answer!!!")
else:
    print("Yes, that's the correct answer!!!")

age_b = 21

age_g = 18

if age_b >= 21 and age_g >= 18:
    print("Both Boy and Girl are Eligible for VOTE !!!")
else:
    print("Nope they can't vote as one family member is underage!!!")
    

age_m = 30
age_w = 25

if age_m >=30 or age_w >= 20:
    print("Any one of Man or Women age can be in range 30 or 25 !!!")
else:
    print("Neither Man or Women age is 30 ro 25")

places = ['bengaluru','mysuru','kolara','hubali','chamarajnagara']

place='hubali'

if place in places:
    print("Yes you are right, the place is in the places list :: ",place)
else:
    print("Nope wrong place, Ignore the place")


in_list = 'bidar'

if in_list in places:
    print("Mentioned Place is indeed in list")
else:
    print("Mentioned Place is :: ",in_list)
    print("Is not part of the list")

breakfast = [ 'idly', 'pongal', 'vade', 'masala dosai', 'puri' ]

item = 'rave dosai'

if item not in breakfast:
    print("rave dosai is not in menu")
else:
    print("rave dosai is in menu")

