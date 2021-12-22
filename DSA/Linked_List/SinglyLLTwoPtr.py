
class Node:
    def __init__(self,Data):
        self.Data=Data
        self.Next=None
    
class SinglyLL:
    def __init__(self):
        self.Head=None
        self.__Tail=None
        self.__cnt=0
    
    def insertfirst(self,Data):
        Newn=Node(Data)
        if self.Head==None:
            self.__Tail=Newn
        else:
            Newn.Next=self.Head
            
        self.Head=Newn
        self.__cnt+=1

    def insertlast(self,Data):
        Newn=Node(Data)
        if self.Head==None:
            self.Head=Newn
        else:
            self.__Tail.Next=Newn

        self.__Tail=Newn
        self.__cnt+=1
    def insertatpos(self,Data,pos):
        if pos<1 or pos>self.__cnt+1:
            print("Invalid Position")
            return 
        if pos==1:
            self.insertfirst(Data)
            return
        if pos==self.__cnt+1:
            self.insertlast(Data)
            return
        else:
            Newn=Node(Data)
            temp=self.Head
            count=1
            while count<pos-1:
                temp=temp.Next
                count+=1
            Newn.Next=temp.Next
            temp.Next=Newn
        self.__cnt+=1
    
    def getfirst(self):
        if self.Head==None:
            return"empty list"
        return self.Head.Data
    
    def getlast(self):
        if self.Head==None:
            return"empty list"
        return self.__Tail.Data

    def getatpos(self,pos):
        if pos<1 or pos>self.__cnt:
            return "Invalid Position"
        if pos==1:
            return self.getfirst()
        if pos==self.__cnt:
            return self.getlast()
        else:
            temp=self.Head
            count=1
            while count<pos:
                temp=temp.Next
                count+=1
            return temp.Data

    def deletefirst(self):
        if self.Head==None:
            print("empty list")
            return 
        
        if self.Head.Next==None:
            self.Head=None
            self.__Tail=None
        else:
            self.Head=self.Head.Next
        
        self.__cnt-=1

    def deletelast(self):
        if self.Head==None:
            print("empty list")
            return 
        
        if self.Head.Next==None:
            self.Head=None
            self.__Tail=None
        else:
            temp=self.Head
            while temp.Next.Next!=None:
                temp=temp.Next
            temp.Next=None
            self.__Tail=temp
        
        self.__cnt-=1
    def deleteatpos(self,pos):
        if pos<1 or pos>self.__cnt:
            print("Invalid Position")
            return 
        if pos==1:
            self.deletefirst()
            return
        if pos==self.__cnt:
            self.deletelast()
            return
        else:
            temp=self.Head
            count=1
            while count<pos-1:
                temp=temp.Next
                count+=1
            temp.Next=temp.Next.Next
        self.__cnt-=1

    def insertatindex(self,Data,index):
        self.insertatpos(Data,index+1)
    
    def deleteatindex(self,index):
        self.deleteatpos(index+1)
    
    def getatindex(self,index):
        return self.getatpos(index+1)

    def __update(self,Data,pos):
        if pos<1 or pos>self.__cnt:
            print("Invalid Position")
            return 
        temp=self.Head
        count=1
        while count<pos:
            temp=temp.Next
            count+=1
        temp.Data=Data

    #linked list reversed without changing Next pointer (Data iterative)
    def ReverseLL(self):
        start=1
        end=self.__cnt

        while start<end:
            no1=self.getatpos(start)
            no2=self.getatpos(end)
            self.__update(no2,start)
            self.__update(no1,end)
            start+=1
            end-=1

    #linked list reversed with changing Next pointer (pointer iterative)    
    def ReverseLLX(self):
        self.__Tail=self.Head
        temp=self.Head
        temp2=None
        while temp!=None:
            temp1=temp.Next
            temp.Next=temp2
            temp2=temp
            temp=temp1
        self.Head=temp2

    def display(self):
        if self.Head==None:
            print("empty list")
            return
        
        temp=self.Head
        while temp!=None:
            print(temp.Data,end=" ")
            temp=temp.Next
        print()

    #linked list to stack adapter here time complexity for pop and top will be o(n)
    def push(self,Data):
        self.insertlast(Data)
    
    def pop(self):   #time complexity for that pop will be O(n)
        self.deletelast()
    
    def top(self):
        return self.getlast()

    #linked list to stack adapter here time complexity for pop and top will be o(1) (best approach)
    def push1(self,Data):
        self.insertfirst(Data)
    
    def pop1(self):   #time complexity for that pop will be O(1)
        self.deletefirst()
    
    def top1(self):
        return self.getfirst()

    def size(self):
        return self.__cnt
    
    #linked list to que adapter
    def add(self,Data):
        self.insertlast(Data)
    
    def remove(self):
        self.deletefirst()
    
    def peek(self):
        return self.getfirst()

    #Find kth index of element from end of the linked list without using size and use iterative method in one traversal end starts with 0 index

    def findKth(self,k):
        if self.Head==None:
            return "Linked List is empty"
        if k<0:
            return "invalid k"
        i=self.Head
        j=self.Head
        result=""
        for item in range(k):
            j=j.Next
            if j==None:
                result="invalid k"
                break
        if result!="":
            return result
        while j.Next!=None:
            i=i.Next
            j=j.Next
        return i.Data
    
    #Find middle of element from end of the linked list without using size and use iterative method in one traversal 

    def middle(self):
        if self.Head==None:
            return "Linked List is empty"
        i=self.Head
        j=self.Head
        while j!=None and j.Next!=None:
            i=i.Next
            for k in range(2):
                j=j.Next
        return i.Data

    #merge two sorted linked list
def mergeSortedLL(l1,l2):
    temp1=l1.Head
    temp2=l2.Head
    obj=SinglyLL()
    while temp1!=None and temp2!=None:
        if temp1.Data<=temp2.Data:
            obj.insertlast(temp1.Data)
            temp1=temp1.Next
        else:
            obj.insertlast(temp2.Data)
            temp2=temp2.Next
    if temp1==None:
        while temp2!=None:
            obj.insertlast(temp2.Data)
            temp2=temp2.Next
    elif temp2==None:
        while temp1!=None:
            obj.insertlast(temp1.Data)
            temp1=temp1.Next
    return obj

obj=SinglyLL()
obj.display()
print(obj.size())
obj.deletefirst()
obj.deletelast()
obj.insertfirst(65)
obj.insertfirst(6)
obj.insertlast(44)
obj.insertlast(94)
obj.insertlast(4)
obj.display()
print(obj.size())
obj.deletefirst()
obj.display()
print(obj.size())
obj.deletelast()
obj.deletelast()
obj.deletelast()
obj.deletelast()
obj.display()
print(obj.size())
obj.insertatpos(55,1)
obj.insertatpos(35,2)
obj.insertatpos(12,2)
obj.insertatpos(10,2)
obj.insertatpos(20,2)
obj.insertatpos(30,2)
obj.insertatpos(30,20)
obj.insertatpos(30,0)
obj.display()
print(obj.size())
#obj.deleteatpos(5)
#obj.deleteatpos(1)
#obj.deleteatpos(2)
#obj.deleteatpos(2)
#obj.deleteatpos(20)
#obj.deleteatpos(0)
obj.display()
print(obj.size())
print(obj.getfirst())
print(obj.getlast())
print(obj.getatpos(2))
print(obj.getatpos(20))
print(obj.getatpos(-2))
print(obj.getatpos(0))
obj.display()
#obj.update(600,3) #private function
obj.display()
obj.ReverseLL()
obj.display()
obj.deletefirst()
obj.ReverseLL()
obj.display()
obj.ReverseLLX()
obj.display()
obj.insertatpos(655,6)
obj.insertatpos(5,4)
obj.ReverseLLX()
obj.display()
obj.ReverseLL()
obj.display()
obj.insertatindex(966,3)
obj.display()
obj.deleteatindex(2)
obj.display()
print(obj.getatindex(-1))

#linked List to stack adapter time complexity O(N) for pop and top
print()
print("linked list to Stack ")
ob=SinglyLL()
ob.pop()
ob.display()
print(ob.size())
ob.push(52)
ob.push(66)
ob.push(66)
ob.push(96)
ob.display()
print(ob.size())
print(ob.top())
ob.pop()
ob.pop()
ob.display()
print(ob.top())

#linked list to Que
print()
print("Linked List to Que")
print()
que=SinglyLL()
que.remove()
que.display()
print(que.size())
que.add(12)
que.add(12)
que.add(1)
que.add(17)
que.add(19)
que.add(15)
que.display()
print(que.size())
print(que.peek())
que.remove()
que.remove()
que.remove()
que.remove()
que.remove()
print(que.peek())
que.add(17)
que.add(19)
que.add(15)
que.display()
print(que.size())

#linked List to stack adapter time complexity O(1) for pop and top
stack=SinglyLL()
stack.pop1()
stack.display()
print(stack.size())
print(stack.top1())

stack.push1(65)
stack.push1(695)
stack.push1(5)
stack.push1(6)
stack.push1(69)
stack.push1(64)
stack.display()
print(stack.top1())
stack.pop1()
stack.display()

#Find kth index of element from end of the linked list without using size and use iterative method in one traversal end starts with 0 index

print(stack.findKth(0))
print(stack.findKth(5))

#Find middle of element of the linked list without using size and use iterative method in one traversal 
dd=SinglyLL()
dd.insertfirst(65)
# dd.insertfirst(56)
# dd.insertfirst(19)
# dd.insertfirst(94)
# dd.insertfirst(900)
# dd.insertfirst(89)
# dd.insertfirst(89)
print(dd.middle())

#merge two sorted LL

obj1=SinglyLL()
obj1.insertlast(2)
obj1.insertlast(5)
obj1.insertlast(7)
obj1.insertlast(8)
obj1.insertlast(9)
obj1.insertlast(13)
obj1.insertlast(14)
obj1.insertlast(20)

obj2=SinglyLL()
obj2.insertlast(1)
obj2.insertlast(3)
obj2.insertlast(4)
obj2.insertlast(8)
obj2.insertlast(10)
obj2.insertlast(11)
obj2.insertlast(12)
obj2.insertlast(15)
obj2.insertlast(16)
obj2.insertlast(17)
obj2.insertlast(19)


res=mergeSortedLL(obj1,obj2)
res.display()