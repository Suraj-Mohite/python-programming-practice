"""
2.	Declare a list in python and assign [4,5,1,2,4,7,1,2,5,7,6,6,8]. Create a tuple from the list where all the values are unique and added 100 at the end and print it. i.e.
Input = [4,5,1,2,4,7,1,2,5,7,6,6,8]
Possible Output = (1,2,4,5,6,7,8,100)
The order of the elements 1,2,4,5,6,7,8 can be anything, but 100 should the last element of the tuple.
"""

def Tuple_Function(List1):
    var= list(set(List1))
    var.append(100)
    return tuple(var)

List1=[4,5,1,2,4,7,1,2,5,7,6,6,8]

print(Tuple_Function(List1))