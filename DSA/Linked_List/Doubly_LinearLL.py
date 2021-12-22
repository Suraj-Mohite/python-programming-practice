
class Node:
    def __init__(self,Data):
        self.Data=Data
        self.Next=None
        self.Prev=None

class Doubly_LinearLL:
    def __init__(self):
        self.__Head=None
        self.__cnt=0
    
    def InsertFirst(self,Data):
        Newn=Node(Data)
        if self.__Head==None:
            self.__Head=Newn
        else:
            Newn.Next=self.__Head
            self.__Head.Prev=Newn
            self.__Head=Newn
        self.__cnt+=1
    
    def InsertLast(self,Data):
        Newn=Node(Data)
        if self.__Head==None:
            self.__Head=Newn
        else:
            Temp=self.__Head
            while Temp.Next!=None:
                Temp=Temp.Next
            Newn.Prev=Temp
            Temp.Next=Newn
        self.__cnt+=1

    def InsertAtPos(self,Data,Pos):
        
        if Pos<=0 or Pos>self.__cnt+1:
            print("ERROR:Not Valid Position")
            return
        if Pos==1:
            self.InsertFirst(Data)
            return
        if Pos==self.__cnt+1:
            self.InsertLast(Data)
            return
        
        Temp=self.__Head
        Newn=Node(Data)
        Counter=1
        while Counter<Pos-1:
            Temp=Temp.Next
            Counter+=1
        Newn.Next=Temp.Next
        Temp.Next.Prev=Newn
        Newn.Prev=Temp
        Temp.Next=Newn
        self.__cnt+=1

    def DeleteFirst(self):
        if self.__Head==None:
            print("List is Empty")
            return
        elif self.__Head.Next==None:
            self.__Head=None
        else:
            self.__Head=self.__Head.Next
            self.__Head.Prev=None

        self.__cnt-=1

    def DeleteLast(self):
        if self.__Head==None:
            print("Linked list is empty.")
            return
        elif self.__Head.Next==None:
            self.__Head=None
        else:
            Temp=self.__Head
            while Temp.Next.Next!=None:
                Temp=Temp.Next
            Temp.Next=None
        self.__cnt-=1

    def DeleteAtPos(self,Pos):
        if self.__Head==None:
            print("Linked list is empty")
            return
        elif Pos<=0 or Pos>self.__cnt:
            print("ERROR: Invalid Position")
            return
        if Pos==1:
            self.DeleteFirst()
            return
        if Pos==self.__cnt:
            self.DeleteLast()
            return
        Temp=self.__Head
        Counter=1
        while Counter<Pos-1:
            Temp=Temp.Next
            Counter+=1
        Temp.Next.Next.Prev=Temp
        Temp.Next=Temp.Next.Next
        self.__cnt-=1

    def Display(self):
        if self.__Head==None:
            print("Linked list is empty")
            return
        else:
            Temp=self.__Head
            while Temp!=None:
                print(f"|{Temp.Data}|<->",end="")
                Temp=Temp.Next
            print(None)

    def Count(self):
        return self.__cnt

if __name__=="__main__":
    obj=Doubly_LinearLL()
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
        print("9. To Exit")

        try:
            
            inp=int(input("Choose Option..."))
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
                Data=int(input("Enter the Data To Insert At Position"))
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