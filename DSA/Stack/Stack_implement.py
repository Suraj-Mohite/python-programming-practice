class Node:
    def __init__(self,Data):
        self.Data=Data
        self.Next=None

class Stack:
    def __init__(self):
        self.__start=None
        self.__Cnt=0

    def Push(self,Data):

        Newn=Node(Data)
        if self.__start==None:
            self.__start=Newn
        else:
            Temp=self.__start
            while Temp.Next!=None:
                Temp=Temp.Next
            Temp.Next=Newn
        self.__Cnt+=1

    def Pop(self):
        if self.__start==None:
            print("Stack is Empty.")
            return
        if self.__start.Next==None:
            self.__start=None
        else:
            Temp=self.__start
            while Temp.Next.Next!=None:
                Temp=Temp.Next
            Temp.Next=None
        self.__Cnt-=1
    def Peep(self):
        if self.__start==None:
            return "Empty Stack"
             
        else:
            Temp=self.__start
            while Temp.Next!=None:
                Temp=Temp.Next
        return Temp.Data
    
    def Display(self):
        if self.__start==None:
            print("Stack is Empty.")
            return
        Temp=self.__start
        while Temp!=None:
            print(f"|{Temp.Data}|->",end="")
            Temp=Temp.Next
        print()

    def Count(self):
        return self.__Cnt


if __name__=="__main__":
    obj=Stack()
    print(obj.Count())
    print(obj.Peep())
    obj.Push(65)
    print(obj.Count())
    print(obj.Peep())
    obj.Push(44)
    print(obj.Count())
    print(obj.Peep())
    obj.Push(22)
    obj.Push(22)
    obj.Push(298)
    obj.Push(55)
    print(obj.Count())
    print(obj.Peep())
    obj.Display()
    obj.Pop()
    print(obj.Peep())
    obj.Display()
    obj.Push(22)
    obj.Push(22)
    obj.Push(298)
    obj.Push(55)
    obj.Display()
