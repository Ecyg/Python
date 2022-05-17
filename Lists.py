"""
Lists are used to store multiple items
in a single variable

Lists are one of 4 built-in data types
in PYthon used to store eollections
of data.

List
Tuple
Set
Dictionary

"""

mylist = ["apple", "banana", "cherry"]
print(mylist) 

"""
List items are ordered, changeable,
and allows duplicate values

List items are indexed starting at
0

Lists can contain any data type and
contain multiple data types

"""

#list() constructor
thislist = list(("x", "y", "z"))
print(thislist)


"""
List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
Dictionary is a collection which is ordered** and changeable. No duplicate members.


"""

#List items are indexed like arrays
print()
print(mylist[1])

#All index rules apply
#Boolean rules apply too
if "apple" in mylist:
    print("Hell yes")

#Changing Item Value in list

thislist[1] = "a"
print(thislist)

#Change a range of items in a list
thislist[:3] = ["q", "w", "e"]
print(thislist)

#Insert a new item into list
thislist.insert(3, "y")
print(thislist)

#Append an item into list
thislist.append("p")
print(thislist)

# remove() removes an item by value

# pop() removes an item by index
# if no index is given, then the last
# item is removed


# clear() empties the list