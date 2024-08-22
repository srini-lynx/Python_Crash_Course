#!/usr/bin/python
#####################################
#Store a person's name, and include some whitespace characters at the beginning and end of the name. Make sure you use
#each character combination, "\t" and "\n", at least once.
#print the name once, so the whitespace around the name is displayed. Then print the name using each of the three 
#stripping functions, lstrip(), rstrip(), and strip().
#####################################

pname ="  Deeptha\t Srinivasa  \n"
print("------------------------------------")
print("Person Name including whitespace,tab and newline chars :: "+pname)
print("------------------------------------")
print("Person Name using lstrip() :: "+pname.lstrip())
print("Person Name using rstrip() :: "+pname.rstrip())
print("Person Name using strip()  :: "+pname.strip())

