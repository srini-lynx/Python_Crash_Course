#!/usr/bin/python
# Example for sort(), which sort's the list permanently in ascending/descending order

cars = [ 'toyota', 'hundayi', 'bmw', 'mercede','cadillac','ford','audi' ]
print("--------------------------------------------------------------")
print("Cars list contanins the below cars::")
print(cars)
print("--------------------------------------------------------------")
print("After sort() Applied, which by default sorts in ascending order..")
cars.sort()
print("--------------------------------------------------------------")
print(cars)
print("--------------------------------------------------------------")
print("After sort(reverse=True), which sorts in reverse order contents ..")
cars.sort(reverse=True)
print(cars)
print("--------------------------------------------------------------")

#Sorting , but not modifying the order within the list, only the output is affected
motors = [ 'ritz', 'pulsar', 'bajaj','honda','dio','enfield','yamaha', 'kawasaki' ]
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("List motors contents are :: ")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print(motors)
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("After sorted() used on motors list, the contents are ")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print(sorted(motors))
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("Please check below motors list are same as it was before, as sorted() won't change the list")
print(motors)
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
