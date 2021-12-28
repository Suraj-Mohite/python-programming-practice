# f=open('abc.txt','x+')
# print("file name",f.name)
# print("file mode",f.mode)
# print("file is readable",f.readable())
# print("file is writable",f.writable())
# print("file is closed",f.closed)

# f.close()
# print("file is closed",f.closed)

#write data in file
#f.write(str)
#f.writelines(list)

# f=open("abc.txt",'w') #it delete previous data 
# f=open("abc.txt",'a')
# f.write("Suraj\n")
# f.write("prakash\n")
# f.write("mohite\n")
# f.close()

# print("write operation completed")

#write lines
# f=open("../abc1.txt",'w')
# l=("suraj\n","prakash\n","mohite\n","from mumbai")
# f.writelines(l)   #we can pass list,tuple,set as an argument if we pass set then sequense of    output is not fix
# f.close()
# print("write operation completed")

f=open('S:\\inputs\\'+'sss.txt')
print(f.read())

