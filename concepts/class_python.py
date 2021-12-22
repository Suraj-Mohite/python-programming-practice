#Creating class in python

class A:
    #private variables/class or static variables
    __no=None
    __no2=None
    #public/class or static variable
    public="suraj"
    _var=65
    def __init__(self):
        self.__no=500
        self.__no2=32.

    #private function
    def __display(self):
        return (self.__no + self.__no2)

    def _Protected_Fun(self):
        print("inside protected function")
    def fun(self):
        return self.__display()
class B(A):
    pass

o=A()
print(o.fun())

print(o.public)
print(A.public)
print(o._A__display())

o1=B()
print(o._var)
#print(o.__no)
#print(o1.__no)

o1._Protected_Fun()
o._Protected_Fun()
