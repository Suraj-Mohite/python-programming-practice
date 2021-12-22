def BaseToDecimal(no,base):
    if no<0:
        no=-no
    i=0
    add=0
    while no!=0:
        rem=no%10
        add+=(rem*base**i)
        no//=10
        i+=1
    return add

print(BaseToDecimal(111001,2))
print(BaseToDecimal(355,7))
print(BaseToDecimal(355,8))
print(BaseToDecimal(3231,4))
