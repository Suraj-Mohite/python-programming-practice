#Accept Decimal Number and any base and convert that number into entered base

def DecimalToBase(no,base):
    if no<0:
        no=-no
    i=0
    add=0
    while no!=0:
        rem=no%base
        add+=(rem*10**i)
        no//=base
        i+=1
    return add

print(DecimalToBase(694,8))
print(DecimalToBase(57,2))
print(DecimalToBase(-6396,7))
