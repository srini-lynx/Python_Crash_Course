#!/usr/bin/python
##############################################################################################################################
#5-6. Stages of Life: Write an if-elif-else chain that determines a person's stage of life. Set a value for the variable age,
#     and then:
#==>  if the person is < 2 years old, print a message that the person is a baby.
#==>  if the person is >= 2 and < 4 years, print a message that the person is a toddler.
#==>  if the person is >= 4 and < 13 years, print a message that the person is a kid.
#==>  if the person is >= 13 and < 20 years, print a message that the person is a teenager.
#==>  if the person is >= 20 and < 65 years, print a message that the person is a Adult.
#==>  if the person is >= 65 years, print a message that the person is an Elder Citizen.
#     To check the output change the value of s_life and check the output
#     One Caviet is that, since else is used, as it matches all which is not matched by if, even any value other than number
#     Still we get the output as Elder Citizen.
##############################################################################################################################

#s_life = 0x88472 
#s_life = 1 
#s_life = 2 
#s_life = 3 
#s_life = 4
#s_life = 19
#s_life = 20
#s_life = 64
s_life = 65

if s_life < 2:
    print("According to Person Age, Person is a Baby!!!")
elif s_life >=2 and s_life < 4:
    print("According to Person Age, Person is a Toddler!!!")
elif s_life >= 4 and s_life < 13:
    print("According to Person Age, Person is a Kid!!!")
elif s_life >= 13 and s_life < 20:
    print("According to Person Age, Person is a Teenager!!!")
elif s_life >= 20 and s_life < 65:
    print("According to Person Age, Person is a Adult !!!")
else:
    print("According to Person Age, Person is a Elder Citizen!!!")
