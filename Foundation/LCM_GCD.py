#Accept two numbers from user and print their GCD and LCM

def GCD_LCM(no1,no2):
    if no1<=0 or no2<=0:
        return
    lcm=1
    i=2
    temp1=no1
    temp2=no2
    while(no1!=1 or no2!=1):
        if no1%i==0 or no2%i==0:
            lcm*=i
        else:
            i+=1
            continue
        if no1%i==0:
            no1//=i
        if no2%i==0:
            no2//=i

    gcd=1
    i=2
    no1=temp1
    no2=temp2
    while no1!=1 and no2!=1:
        if no1%i==0 and no2%i==0:
            gcd*=i
            no1//=i
            no2//=i
        else:
            i+=1
        if i>min(temp1,temp2):
            break
    if gcd!=1:
        return lcm,gcd
    else:
        if temp1==1 or temp2==1:
            return lcm,1   #if input is 1,1 1,5 6,1 gcd will be 1

            
#approach2
#lcm=no1*no2/gcd
def GCD_LCMX(no1,no2):
    if no1<=0 or no2<=0:
        return
    temp1=no1
    temp2=no2
    while no1%no2!=0:
        rem=no1%no2
        no1,no2=no2,rem
    gcd=no2
    no1,no2=temp1,temp2
    lcm=(no1*no2)//gcd
    return lcm,gcd

print("LCM and GCD ",GCD_LCM(36,24))
print("LCM and GCD ",GCD_LCMX(36,24))
