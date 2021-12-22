
# l=[1,2,2,5,6,4,4,4,4,5,3,3,3,3,3,3,2]
# dict1={}
# for i in l:
#     dict1[i]=dict1.get(i,0)+1

# print(dict1) 

# ternery operator

# a=56
# b=6
# print(a if a>b else b)
# print("both are equal" if a==b else "a greater than b" if a>b else "a smaller than b")
# print((b,a)[a>b])
# print({True:a,False:b}[a>b])
# print((lambda:b,lambda:a)[a>b]())

# b=[4,8,9,7]
# print(id(b))

#string

# st=list("hjgSFDSDRsxgakdgk")
# st=" ".join(st)
# print(st)

#list

l=[1,2,33,3,3,3,4,5,6,7,8,9]
l.insert(5,56)
print(l)
l.sort()
print(l)