def fact(no):
    mult=1
    while no>0:
        mult=mult*no
        no=no-1
    return mult

print(fact(1))