#enter file name dynamically
#enter data in each file dynamically
# fname=input("enter file name.")
def fileTask():
    try:
        # f=open('S:\\inputs\\'+fname,'w+')

        data=input("Enter data")
        f.write(data)
    except FileExistsError as e:
        print("file name already exists .\nenter another name..")
        fileTask()
    else:
        f.close()


# fileTask()

#read data 
# f=open('S:\\inputs\\'+fname)
# # f=open('S:\\inputs\\'+'sss.txt')
# # print(f.read())
# # print(f.read(5))
# # print(f.readline())
# print(f.readlines())


#with statement

# with open('S:\\inputs\\'+fname,'w') as f:
#     f.write("Suraj0\n")
#     f.write("Suraj1\n")
#     f.write("Suraj2\n")
#     f.write("Suraj3\n")
#     f.write("Suraj4\n")
#     f.write("Suraj5\n")

#     print("is closed",f.closed)
# print("is closed",f.closed)

with open('S:\\inputs\\'+'asdf.txt') as f:
    # while(True):
    #     line=f.readline()
    #     if not line:
    #         break
    #     print(line,end="")

    # print(f.tell())
    # print(f.read(3))
    # print(f.tell())
    f.seek(3)
    print(f.tell())
    print(f.read(2))
    f.seek(5)
    print(f.tell())
    print(f.read(2))
    