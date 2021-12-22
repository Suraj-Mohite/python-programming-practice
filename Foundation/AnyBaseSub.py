def AnyBaseSub(no1,no2,base):
    quo=0
    result=0
    i=0
    while no1!=0 or no2!=0 or quo!=0:
        rem1=no1%10
        rem2=no2%10
        if rem1<(rem2+quo):
            rem1+=base
            result+=(rem1-(rem2+quo))*10**i
            quo=1
        else:
            result+=(rem1-(rem2+quo))*10**i
            quo=0
        i+=1
        no1//=10
        no2//=10
    return result

"""def AnyBaseSub(n1,n2,b):
    rv=0
    c=0
    p=1
    while n1>0:
        d1=n1%10
        n1//=10
        d2=n2%10
        n2//=10
        d1+=c
        if d1>=d2:
            c=0
            d=d1-d2
        else:
            c=-1
            d=d1+b-d2
        rv=rv+d*p
        p*=10
    return rv"""

print(AnyBaseSub(1212,256,8))
print(AnyBaseSub(256,202,8))
print(AnyBaseSub(999,111,8))
print(AnyBaseSub(1111,777,8))