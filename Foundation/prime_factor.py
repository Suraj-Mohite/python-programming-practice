def prime_factor(no):
    i=2
    while no!=1:
        if no%i==0:
            print(i,end=" ")
            no//=i
        else:
            i+=1

prime_factor(220)