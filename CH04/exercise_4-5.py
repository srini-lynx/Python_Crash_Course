#!/usr/bin/python
########################################################################
#4-5. Summing a Million:
#     Make a list of the numbers from one to one million, and then use min()
#     and max() to make sure your list actually starts at one and ends at
#     one million. Also, use the sum() function to see how quickly Python
#     can add a million numbers.
########################################################################

million_nums = [ num for num in range(1,10**6+1) ]

print("-----------------------------------------------------------------")
print("List of million_num Content::")
print(million_nums)
print("-----------------------------------------------------------------")

min_million =  min(million_nums)
max_million =  max(million_nums)
sum_million =  sum(million_nums)
print("-----------------------------------------------------------------")
print("Minimum Element in million_num List :: ")
print(min_million)
print("-----------------------------------------------------------------")
print("Maximum Element in million_num List :: ")
print(max_million)
print("-----------------------------------------------------------------")
print("Sum of Elements in million_num List :: ")
print(sum_million)
print("-----------------------------------------------------------------")
