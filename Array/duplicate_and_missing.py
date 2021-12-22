#accept 1 to N number from user and disply missing and duplicate number from that (Array rearrangement ALLOWED)
#[1,5,2,4,5]

def One_Missing_Duplicate(List1):
    print(List1)        
    i=0
    while(i<len(List1)):
        no=List1[i]-1
        if List1[i]!=List1[no]:
            List1[i],List1[no]=List1[no],List1[i]
        else:
            i+=1        
                   
    print(List1)        
    for i in range(len(List1)):
        if List1[i]!=i+1:
            print("Duplicate Number is: ",List1[i])
            print("Missing Number is: ",i+1)
            break
    else:
        print("No missing and duplicate number")


One_Missing_Duplicate([1,5,2,4,5,3])