# Inheritance ==> Acquiring all the attributes (Variables 0 and(Behaviour)  Method From one class to another Calssis
# called Inheritance
# Objective of Inheritance ==> 1) Code Re-Usability 2) Avoid Duplication

# Types of Inheritance
# 1) Single Level Inheritance
# 2) Multi-Level Inheritance
# 3) Hierarchy Inheritance
# 4) Multiple Inheritance


# Ex 1 Single Inheritance

class myClassA:  # Parent Class
    def func(self):
        print("This is method of myClassA")


class myclassB(myClassA):  # Child Class
    def func1(self):
        print("this is method Of myClassB")


mcb = myclassB()
mcb.func()  # this is method of myClassA
mcb.func1()  # this is method Of myClassB


# Ex single Inheritance

class myclassA:
    x, y = 10, 20

    def add(self):
        print(self.x + self.y)


class myclassB(myclassA):
    a, b = 30, 40

    def sub(self):
        print(self.a - self.b)


mcb = myclassB()
mcb.add()  # 30
mcb.sub()  # -10


# Multilevel inheritance

class myclassA:
    x, y = 10, 20

    def add(self):
        print(self.x + self.y)


class myclassB(myclassA):  # myClassB ==> Extends myClassA
    a, b = 30, 40

    def sub(self):
        print(self.a - self.b)


class myClassC(myclassB):  # myClassC ==> Extends myClassB
    c, d = 5, 6

    def mul(self):
        print(self.c * self.d)


mcC = myClassC()
mcC.add()  # 30
mcC.sub()  # -10
mcC.mul()  # 30


# Ex Hierarchy Inheritance One Parent Class has multiple Child class

class myclassA:
    x, y = 10, 20

    def add(self):
        print(self.x + self.y)


class myclassB(myclassA):  # myClassB ==> Extends myClassA
    a, b = 30, 40

    def sub(self):
        print(self.a - self.b)


class myClassC(myclassA):  # myClassC ==> Extends myClassA
    c, d = 5, 6

    def mul(self):
        print(self.c * self.d)


mcB = myclassB()
mcB.sub()  # -10
mcB.add()  # 30
mcC = myClassC()
mcC.add()  # 30
mcC.mul()  # 30


# Ex Multiple inheritance


class myclassA:
    x, y = 10, 20

    def add(self):
        print(self.x + self.y)


class myclassB:
    a, b = 30, 40

    def sub(self):
        print(self.a - self.b)


class myClassC(myclassA, myclassB):  # myClassC ==> Extends myClassA and myClass
    c, d = 5, 6

    def mul(self):
        print(self.c * self.d)


mcC = myClassC()
mcC.add()  # 30
mcC.sub()  # -10
mcC.mul()  # 30


# Ex Invoking parent class method from child class method (Method name is same) using super() Function
# In short it is Overriding Concept

class myClassA:
    def method1(self):
        print("This is parent Class Method")


class myClassB(myClassA):
    def method1(self):
         print("This is Child Class Method")
         super().method1()


mc = myClassB()
mc.method1()  # This is parent Class Method


# Ex

class myclassA:
    i, j = 20, 10  # Class Variables


class myclassB(myclassA):
    a, b = 30, 40  # Class Variables

    def func(self, x, y):  # Local Variables
        print(x + y)
        print(self.a + self.b)  # Class Variables
        print(self.i + self.j)  # Class Variables


mcobj = myclassB()
mcobj.func(33, 44)


# Overriding Variables

class A:
    name = "Abhijeet"


class B(A):
    name = "Anuradha"


obj = B()
print(obj.name)  # Anuradha


# Approach 2
class A:
    name = "Abhijeet"


class B(A):
    name = "Anuradha"

    def func(self):
        print(super().name)  # Calling Parent class variable


obj = B()
print(obj.name)
obj.func()


# Overriding the method Overriding should occur in two class Inheritance must be there


class RBI:
    def rateOfIntrest(self):
        return 10


class SBI(RBI):
    def rateOfIntrest(self):
        return 20


class BOM(RBI):
    def rateOfIntrest(self):
        return 30


sbiobj = SBI()
s = sbiobj.rateOfIntrest()
print(s)

bomObj = BOM()
b = bomObj.rateOfIntrest()
print(b)


# Overloading (Polymorphism)

class Human:
    def sayHello(self, name=None):
        if name is not None:
            print("Hello  " + name)
        else:
            print("Please Give Valid Name")


obj = Human()
obj.sayHello()
obj.sayHello("Neelam")


# Ex 2 for Polymorphism One method having Different parameter

class Calculation:
    def add(self, a=0, b=0, c=0):
        print(a + b + c)


cal = Calculation()
cal.add()
cal.add(10, 20)
cal.add(10, 20, 30)
