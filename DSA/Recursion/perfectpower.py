def perfectPower(no):
    result=None
    m=2
    while(m*m <=no):
        n=2
        while(n*n <=no):
            if(m**n==no):
                result=[m,n]
                break
            n+=1
        
        if(result !=None):
            break
        m+=1
    return result

print(perfectPower(25))