#Accept number and drow pattern in febonacci format

def Pattern_Feb(no):
    if no<0:
        return
    first=0
    second=1
    for i in range(1,no+1):
        for j in range(1,i+1):
            if i==1:
                print(first,end=" ")
            elif i==2 and j==1:
                print(second,end=" ")
                k=first+second
                first,second=second,k
            else:
                print(k,end=" ")
                k=first+second
                first,second=second,k
        print(" ")

Pattern_Feb(6)



