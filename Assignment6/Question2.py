'''
2.Let us consider this example ( list written in general format):

ls = [0, 1, 3, 6, 10]

Its following parts:

ls = [0, 1, 3, 6, 10]
ls = [1, 3, 6, 10]
ls = [3, 6, 10]
ls = [6, 10]
ls = [10]
ls = []

The corresponding sums are (put together in a list): [20, 20, 19, 16, 10, 0]

example:
ls = [1, 2, 3, 4, 5, 6] 
parts_sums(ls) -> [21, 20, 18, 15, 11, 6, 0]

ls = [744125, 935, 407, 454, 430, 90, 144, 6710213, 889, 810, 2579358]
parts_sums(ls) -> [10037855, 9293730, 9292795, 9292388, 9291934, 9291504, 9291414, 9291270, 2581057, 2580168, 2579358, 0]

'''

def List_Function(List1):

    if List1==[]:
        return None

    List_Temp=[]
    for i in range(0,len(List1)):
        Sum=0
        for j in range(i,len(List1)):
            Sum+=List1[j]
        List_Temp.append(Sum)
    List_Temp.append(0)

    return List_Temp

No=int(input("Enter the number of element : "))
print()
List1=[]
print("Enter the Elements into the List.")
for item in range(No):
    element=int(input())
    List1.append(element)

Output=List_Function(List1)
print("Entered list : ",List1)
print("Answer : ",Output)

        
