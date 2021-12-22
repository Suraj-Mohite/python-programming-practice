#formula: nC0=1,nCn=1,nCk=n!/k!*(n-k)!
#if we want to find nCk+1=nCk*(n-k)/k+1
def pattern_Per_comb(no):
    for i in range(no):
        val=1
        for j in range(i+1):
            if j==0:
                print(val,end=" ")
            else:
                val=(val*(i-(j-1)))//((j-1)+1)  #Formula 2nd
                print(val,end=" ")
        print()

pattern_Per_comb(7)