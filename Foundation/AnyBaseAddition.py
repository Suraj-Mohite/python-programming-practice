#accept two number and base from user and perform addition

def BaseAddition(no1,no2,base):
    result=0
    i=0
    quo=0
    while no1!=0 or no2!=0 or quo!=0:
        rem1=no1%10
        rem2=no2%10
        if quo+rem1+rem2>=base:
            result+=((quo+rem1+rem2)%base)*10**i
            quo=(quo+rem1+rem2)//base
        else:
            result+=(quo+rem1+rem2)*10**i
            quo=0
        i+=1
        no1//=10
        no2//=10
   

    return result
    
print(BaseAddition(346,777,8))
print(BaseAddition(236,754,8))
print(BaseAddition(888,888,8))
print(BaseAddition(767,421,8))
print(BaseAddition(234,343,5))
print(BaseAddition(333,111,5))
print(BaseAddition(34,343,5))
print(BaseAddition(934,343,10))

