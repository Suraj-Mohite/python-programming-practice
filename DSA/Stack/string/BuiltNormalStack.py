#construct a stack with fixed size __array with all push,pop,top(peep),size,display function if size of stack is full and you push element print Stack overflow error and if size is zero and you pop element thenprint size underflow

class Stack:
    def __init__(self,size):
        self.__arr=[None]*size
        self.__temp=-1

    def Push(self,Data):
        if self.__temp==len(self.__arr)-1:
            print("ERROR:Stack Overflow")
            return
        
        self.__arr[self.__temp+1]=Data
        self.__temp+=1
    
    def Pop(self):
        if self.__temp==-1:
            print("ERROR:Stack underflow")
            return
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


obj=Stack(5)
obj.Push(22)
obj.Push(2)
obj.Push(9)
obj.Push(9)
obj.Push(9)
obj.Push(9)
obj.Display()
print(obj.Size())
obj.Push(56)
obj.Pop()
obj.Pop()
obj.Pop()
obj.Pop()
obj.Pop()
obj.Pop()
obj.Display()
print(obj.Size())
obj.Pop()
