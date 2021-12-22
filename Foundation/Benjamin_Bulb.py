#import math
def Benjamin_bulb(no):
    for i in range(1,no+1):
        #s=int(math.sqrt(i)) #with math library
        s=int(i**0.5)   #without math library
        if(i==s*s):
            print(i,end=" ")

Benjamin_bulb(25)