#impliment static que

class Que:
    def __init__(self,size):
        self.__arr=[None]*size
        self.__temp=-1
        self.__temp2=0
    
    def add(self,Data):
        if self.__temp==len(self.__arr)-1 and self.__temp2==0:
            return "Que Overflow"
        if self.__temp==len(self.__arr)-1 and self.__temp2!=0:
            temp=0
            while self.__arr[temp]!=None:
                temp+=1
            self.__arr[temp]=Data
        else:
            self.__arr[self.__temp+1]=Data
            self.__temp+=1

    def remove(self,Data):
        if self.__arr[self.__temp2]==None:
            return "Que is Empty"
        if self.__arr[self.__temp2]!=None:
            