#x is a global variable


from tkinter import Y


x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()


#But if we have an x variable inside
#the function, that will be used

#We could also use the "global" keyword

def myfunc1():
    global y
    y = "fantastic"
myfunc1()
print("Python is " + y)