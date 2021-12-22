#getmin function with O(1) time complexity

class Stack:
    def __init__(self,size):
        self.__arr=[None]*size
        self.__min=[None]*size    #extra space
        self.__temp=-1
        self.__mintemp=-1

    def Push(self,Data):
        if self.__temp==len(self.__arr)-1:
            arr=[None]*(2*len(self.__arr))
            for i in range(len(self.__arr)):
                arr[i]=self.__arr[i]
            self.__arr=arr
        if self.__mintemp==len(self.__min)-1:
            arr1=[None]*(2*len(self.__min))
            for i in range(len(self.__min)):
                arr1[i]=self.__min[i]
            self.__min=arr1
        
        if self.__mintemp==-1:
            self.__min[self.__mintemp+1]=Data
            self.__mintemp+=1
        elif Data<=self.__min[self.__mintemp]:
            self.__min[self.__mintemp+1]=Data
            self.__mintemp+=1
        
        
        self.__arr[self.__temp+1]=Data
        self.__temp+=1
        
    def getmin(self):
        if self.__mintemp==-1:
            return "stack is empty. NO MIN"
        return self.__min[self.__mintemp]

    def Pop(self):
        if self.__temp==-1:
            print("ERROR:Stack underflow")
            return
        
        if self.__arr[self.__temp]==self.__min[self.__mintemp]:
            self.__min[self.__mintemp]=None
            self.__mintemp-=1

        self.__arr[self.__temp]=None
        self.__temp-=1

    def Size(self):
        return self.__temp+1
    
    def Display(self):
        if self.__temp==-1:
            print("Stack Is Empty")
            return
        for i in range(self.__temp+1):
            print(self.__arr[i],end=" ")
        print()
        print(self.__min)


obj=Stack(5)
print(obj.getmin())
obj.Push(22)
obj.Push(20)
obj.Push(11)
obj.Push(2)

print(obj.getmin())
obj.Push(6)
obj.Push(14)
obj.Push(1)
obj.Pop()
obj.Push(26)
obj.Pop()
print(obj.getmin())
obj.Display()

obj.Push(1)
obj.Push(1)
obj.Push(28)
obj.Push(8)
obj.Push(7)

obj.Pop()
obj.Pop()
obj.Pop()
obj.Pop()
obj.Pop()
obj.Pop()
obj.Pop()
obj.Pop()
obj.Pop()
print(obj.getmin())
obj.Display()
obj.Pop()
obj.Pop()
print(obj.getmin())
