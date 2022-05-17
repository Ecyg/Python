"""

Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview

You can check the data type
through the type() function
"""

x = 1 #Integer
y = 2.8 #Float
z = 1j #Complex

#You can write multiline strings
#with triple single/double quotes

a = """I'm a huge string
multiple lines
god damn."""

print(a)

#Strings are arrays
b = "Hello, World!"
print()
print(b[1])

#Looping through a string
for x in "banana":
    print(x)

#String Length
print()
print(len(b))

#Check for a substring in a string
#Returns a boolean statement
print("Hell" in b)

#Useful in if/else statements
if "Hell" in b:
    print("Nice find!")

#You can use the "not" keyword 
#to see if something is NOT in a string

print("nope" not in b)

#Slicing
print(b[2:5])
print(b[:5]) #Slice from the start
print(b[2:]) #Slice to the end
print(b[-5:-2]) #Negative Indexing

#String Concat
a = "Hello"
b = "World!"
c = a +" " + b
print(c)

#Escaping special characters
q = "Special char \"test\" "
print(q)


#Escaping special characters
"""
\'	Single Quote	
\\	Backslash	
\n	New Line	
\r	Carriage Return	
\t	Tab	
\b	Backspace	
\f	Form Feed	
\ooo	Octal value	
\xhh	Hex value


"""