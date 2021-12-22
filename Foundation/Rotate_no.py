#accept one number and k from user and rotate that number k times

def Rotate_Number(no,k):
    size=len(str(no))

    if k<0:
        while k<-size:
            k=k%size
        k+=size
    while k>size:
        k%=size

    rem=(no%10**k)*10**(size-k)
    rem=rem+no//10**k

    return rem

print(Rotate_Number(51234,-7))

