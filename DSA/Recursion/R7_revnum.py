mult=0
def revNum(n):
    global mult
    if n==0:
        return 0
    if n>0:
        mult=(mult*10)+(n%10)
        revNum(n//10)
        return mult
    if n<0:
        n=-n
        return -revNum(n)
        


print(revNum(-9654))
#print(revNum(-21))

    