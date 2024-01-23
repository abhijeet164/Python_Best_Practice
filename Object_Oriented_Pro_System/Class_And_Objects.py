# Definition of Class ==> A Class is a Logical entity Or Blue Print
# A Class Contain Variables (Attribute) And Method/Function (Behavior)
# Class Does not occupy Space in Memory

# Definition of Object ==>  Object is Instance of a class an a physical entity
# Object Does occupy Space in Memory

# Difference between Method And Class
# Function ==> Piece of Code Written Outside of a Class Declaration  is Known as Function
# Method ==> Piece of Code Written Inside of a Class Declaration  is Known as Method

# For one class we can Create multiple Objects
# But Objects are independent

# Syntax for Creating a class:

class myClass:  # Class creation
    def myFun(self):  # Method Creation
        pass  # Empty method so use pass

    def disp(self):
        print("Hello Python")


mc = myClass()  # Object creation
mc.myFun()  # Method Calling with Object Reference
mc.disp()


# Ex 2 Passing variable inside to method inside  of a class
class myClass:  # Class creation
    def myFun(self):  # Method Creation
        pass  # Empty method so use pass

    def disp(self, name):
        print("Hello mr ", name)


mc = myClass()  # Object creation
mc.myFun()  # Method Calling with Object Reference
mc.disp("Abhijee")


# Ex 3 There are two types of method 1)Instance Method 2) Static Method 1)Instance Method = can be called by object
# reference 2) Static Method = can be called by class name This is achieved by using annotation @staticmethod Qualifier
# and This Staticmethod is Common for Every object

class myClass:
    def func(self):
        print("This Is Instance")

    @staticmethod
    def disp(self, name):  # Here self acts as parameter
        print("This Static method", self, name)


mc = myClass()
mc.func()  # Instance method aces by Object reference
mc.disp("Abhi", "Rane")  # static method access by Object ref but not a good practise
myClass.disp("Vishu", "Rane")  # static variable is Common for all Objects


# Types Of Variable
# 1)Global variable =Declared outside of class can access anywhere
# 2)Class variable= Declared Inside the class and scope is limited to class
# 3)Local Variable =Declared Inside the method or function is called local variable scope is limited to method/function
#  Note Self is a keyword which is always representing a class

# Types of Method
# 1) Instance Method = Can be called only through Object reference
# 2) Static Method = Can be directly called by Class Name And this Method is common for every object


# Ex 1  Accessing class variable into method

class myClass:
    a, b = 10, 20  # Class Level Variable

    def add(self):
        print(self.a + self.b)  # to Access the Class variable use Self KeyWord inside a method

    def mul(self):
        print(self.a * self.b)


mc = myClass()
mc.add()
mc.mul()

# Ex 2 Accessing global Variables inside a method
i, j = 22, 33  # Global Variable


class myClass:
    a, b = 10, 20  # Class Level Variable

    def add(self, x, y):  # Local Variable
        print(x + y)
        print(self.a + self.b)  # to Access the Class variable use Self KeyWord inside a method
        print(i + j)  # Access the Global variable inside a method Directly


mc = myClass()
mc.add(44, 55)

# Ex = Accessing global Variables inside a method which are having same name
a, b = 22, 33


class myClass:
    a, b = 10, 20  # Class Level Variable

    def add(self, a, b):
        print(a + b)
        print(self.a + self.b)  # to Access the Class variable use Self KeyWord inside a method
        print(globals()["a"] + globals()[
            "b"])  # Access the Global variable inside a method Directly  by globals()[Variable name]


mc = myClass()
mc.add(44, 55)


# Creating Multiple Objects and calling Them

class myClass:
    def disp(self, name):
        print("Hello " + name + " How are you")


mc = myClass()
mc.disp("Abhijeet")  # Hello Abhijeet How are you

mc1 = myClass()
mc.disp("Vishwjeet")  # Hello Vishwjeet How are you

mc2 = myClass()
mc.disp("Sourabh")  # Hello Sourabh How are you


# Example for static method
class MyClass:
    def m1(self):
        print("This is instance Method")

    @staticmethod
    def m2(num, num2):
        print("This is Static Method", num, num2)


mc = MyClass()
mc.m1()  # This is instance Method
mc.m2(10, 20)  # This is Static Method 10 20 (Static Method Called by Object Ref)

MyClass.m2(100, 200)  # This is Static Method 100 200(Static Method Called by Class Ref)
