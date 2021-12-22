def Rev(no):
    sum=0
    while(no!=0):
        digit=no%10
        sum=(sum*10)+digit
        no//=10
    return sum

print(Rev(5010065
))