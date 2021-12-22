class Node:
    def __init__(self,Data):
        self.Data=Data
        self.Next=None
        self.Prev=None
    
class Doubly_CircularLL:
    def __init__(self):
        self.__Head=None
        self.__Tail=None
        self.__Cnt=0
    
    def InsertFirst(self,Data):
        #Creating Node
        Newn=Node(Data)
        
        if self.__Head==None:
            self.__Tail=Newn
        else:
            self.__Head.Prev=Newn
            Newn.Next=self.__Head
        self.__Head=Newn
        self.__Head.Prev=self.__Tail
        self.__Tail.Next=self.__Head
        self.__Cnt+=1
    
    def InsertLast(self,Data):
        #Creating Node
        Newn=Node(Data)
        
        if self.__Head==None:
            self.__Head=Newn
        else:
            Newn.Prev=self.__Tail
            self.__Tail.Next=Newn
        self.__Tail=Newn
        self.__Head.Prev=self.__Tail
        self.__Tail.Next=self.__Head
        self.__Cnt+=1
    def InsertAtPos(self,Data,Pos):
        size=self.__Cnt
        if Pos<=0 or Pos>size+1:
            print("ERROR: Invalid Position")
            return
        if Pos==1:
            self.InsertFirst(Data)
            return
        if Pos==size+1:
            self.InsertLast(Data)
            return
        Counter=1
        Newn=Node(Data)
        Temp=self.__Head
        while Counter<Pos-1:
            Temp=Temp.Next
            Counter+=1
        Newn.Next=Temp.Next
        Temp.Next.Prev=Newn
        Newn.Prev=Temp
        Temp.Next=Newn
        self.__Cnt+=1

    def DeleteFirst(self):
        if self.__Head==None:
            print("Empty List")
            return
        elif self.__Head==self.__Tail:
            self.__Head=None
            self.__Tail=None
        else:
            self.__Head=self.__Head.Next
            self.__Head.Prev=self.__Tail
            self.__Tail.Next=self.__Head
        self.__Cnt-=1

    def DeleteLast(self):
        if self.__Head==None:
            print("Empty List")
            return
        elif self.__Head==self.__Tail:
            self.__Head=None
            self.__Tail=None
        else:
            self.__Tail=self.__Tail.Prev
            self.__Tail.Next=self.__Head
            self.__Head.Prev=self.__Tail
        self.__Cnt-=1

    def DeleteAtPos(self,Pos):
        size=self.__Cnt
        if self.__Head==None:
            print("Empty List")
            return
        elif Pos<=0 or Pos>size:
            print("ERROR: Invalid Position")
            return
        if Pos==1:
            self.DeleteFirst()
            return
        if Pos==size:
            self.DeleteLast()
            return
        Counter=1
        Temp=self.__Head
        while Counter<Pos-1:
            Temp=Temp.Next
            Counter+=1
        Temp.Next.Next.Prev=Temp
        Temp.Next=Temp.Next.Next
        self.__Cnt-=1

    def Display(self):
        if self.__Head==None:
            print("Empty List")
            return
        Temp=self.__Head

        while Temp!=self.__Tail:
            print(f"|{Temp.Data}|<->",end="")
            Temp=Temp.Next
        print(f"|{Temp.Data}|<->",end="")
        print()
    
    def Count(self):
        return self.__Cnt


if __name__=="__main__":
    obj=Doubly_CircularLL()
    while(True):
        print("Enter : ")
        print("1. To Insert Element At First Position")
        print("2. To Insert Element At last Position")
        print("3. To Delete Element At First Position")
        print("4. To Delete Element At last Position")
        print("5. To Insert Element At Perticular Position")
        print("6. To Delete Element At Perticular Position")
        print("7. To Display Linked List")
        print("8. To Count Elements of Linked List")
        print("9. To Exit.\n")

        try:
            inp=int(input("Choose Option : "))
            print()
            if inp<=0 or inp>9:
                print("Please select correct Option.")
            elif inp==1:
                Data=int(input("Enter the Data To Insert At First Position"))
                obj.InsertFirst(Data)
            elif inp==2:
                Data=int(input("Enter the Data To Insert At Last Position"))
                obj.InsertLast(Data)
            elif inp==3:
                obj.DeleteFirst()
            elif inp==4:
                obj.DeleteLast()
            elif inp==5:
                Pos=int(input("Enter the Position : "))
                Data=int(input(f"Enter the Data To Insert At {Pos} Position : "))
                obj.InsertAtPos(Data,Pos)
            elif inp==6:
                Pos=int(input("Enter the Position : "))
                obj.DeleteAtPos(Pos)
            elif inp==7:
                obj.Display()
            elif inp==8:
                print("Number of Elements Are ",obj.Count())
            elif inp==9:
                print("Thanks For Using Application")
                break        
        except ValueError as e:
            print("ValueError : Invalid DataType")