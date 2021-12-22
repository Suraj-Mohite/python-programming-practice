

def inverse(no):

    temp=0
    i=1
    while no!=0:
        rem=no%10
        temp+=i*(10**(rem-1))
        i+=1
        no//=10
    return temp

print(inverse(462153))
