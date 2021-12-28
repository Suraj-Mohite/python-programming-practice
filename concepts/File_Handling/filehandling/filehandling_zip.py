from os import name
from zipfile import *

f=ZipFile('filename1211997.zip','w',ZIP_DEFLATED)
f.write('aaa.txt')
f.write('asdf.txt')
f.write('abc.txt')
f.write('ads.txt')
f.write('bbc.txt')
f.close()

f=ZipFile('filename1211997.zip','r',ZIP_STORED)
names=f.namelist()
print(names)

for fname in names:
    print('file name : ',fname)
    f1=open(fname,'r')
    print('content is...')
    print(f1.read())
    print()

f.close()