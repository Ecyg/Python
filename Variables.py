#This is how Python variables work

x = 5 # this is a integer
y = "john" # This is a string
print(x)
print(y)

#Casting data types

x1 = str(3)
y1= int(3)
z1 = float(3)

print()
print(x1)
print(y1)
print(z1)

#Getting the data type
print()
print(type(x))
print(type(y))

#You can use both double quotes
a = "double quotes"
#And single quotes
b = 'single quotes'

#Variable -> Many values to Many Variables
c, d, e = "Orange", "Banana", "Cherry"
print(c)
print(d)
print(e)
print()

#Variables -> 1 value to many variables
c = d = e = "Orange"
print(c)
print(d)
print(e)