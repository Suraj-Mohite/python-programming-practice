
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


def AnyBaseMult(no1,no2,base):
    res_arr=[]
    temp1=no1
    quo=0
    i=0
    j=0
    result=0
    while no2!=0:
        result=0
        rem2=no2%10
        no1=temp1
        while no1!=0 or quo!=0:
            rem1=no1%10
            if (rem2*rem1)+quo>=base:
                result+=(((rem2*rem1)+quo)%base)*10**i
                quo=((rem2*rem1)+quo)//base
            else:
                result+=((rem2*rem1)+quo)*10**i
                quo=0
            i+=1
            no1//=10
        i=0
        result=result*10**j
        res_arr.append(result)
        j+=1
        no2//=10
    #print(res_arr) to check all addition before sending to addition function
    if len(res_arr)>1:
        no1=res_arr[0]
        no2=res_arr[1]
        result=BaseAddition(no1,no2,base)
        for i in range(2,len(res_arr)):
            result=BaseAddition(result,res_arr[i],base)
    return result

print(AnyBaseMult(234,1376,8))
print(AnyBaseMult(234,376,8))
print(AnyBaseMult(234,76,8))
print(AnyBaseMult(234,6,8))