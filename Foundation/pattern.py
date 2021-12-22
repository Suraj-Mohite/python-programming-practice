def pattern(str1):
    if type(str1)!=str:
        return
    if (str1>="A" and str1<="Z") or (str1>="a" and str1<="z"):
        for i in range(1,11):
            if i==1:
                print(f"{str1} * {i} = {str1}")
            else:
                print(f"{str1} * {i} = {str(i)}{str1}")
    else:
        return
pattern("a")