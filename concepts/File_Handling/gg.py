
"""
f1=open('suraj.JPG','rb')
f2=open('xyz.JPG','rb')
f3=open('suraj_append.JPG','ab')

for i in f1:
    f3.write(i)

for i in f2:
    f3.write(i)

f1.close()
f2.close()
f3.close()"""

f=open("gg.py","r")
for i in f:
    print(f.read())