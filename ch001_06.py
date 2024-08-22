#!/usr/bin/python
#Program:: for Striping WhiteSpaces

Var1 = 'Python   '
Var2 = 'More White Spaces to Right     '
print("-------------------------")
print("Var1 Content ::" + Var1)
print("Var2 Content ::" + Var2)
print("-------------------------")
print(Var1 + "Due to spaces in Var1 we can see additional spaces")
print(Var2 + "Due to spaces in Var2 we can see additional spaces")
print(Var1.rstrip() + " After rstrip() on Var1 don't have any additional spaces")
print(Var2.rstrip() + "After  rstrip() on Var2 don't have any additional spaces")
