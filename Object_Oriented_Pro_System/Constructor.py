# Difference Between A Method and Constructor
# Method  : We can Assign Any name to Method and can take argument or Parameter
#           we have to use Object to invoke the Method
# Constructor : Constructor Name is fixed ==> def __init__(self)
#               Constructor will not Return any value
#               Constructor can take Arguments/Parameter
#               Constructor will be called at the time of object creation

class myClass:
    def __init__ (self):
        print("This is constructor")

    def func (self):
        print("This is a method")
    def func2 (self,x,y):
        return x+y

mc=myClass() # this is zero argument constructor
mc.func()
res=mc.func2(20,30)
print(res)

# Constructor Accepting One Argument

class myClass:
    name = "John"  # Class Variable

    def __init__(self, name):
        print(name)  # Local variable
        print(self.name)


mc = myClass("Smith")  # Passing parameter to constructor


# Ex 3
class Employee:
    def __init__(self, eid, ename, esal):
        self.eid = eid
        self.ename = ename
        self.esal = esal
        print(self.eid, self.ename, self.esal)

    def display(self):
        print(self.eid, self.ename, self.esal)


emp = Employee(eid=12, ename="Abhi", esal=500)  # Constructor calling by passing values
emp.display()  # Methode Invoked by Object reference


# Constructor Returning only String data types
class Employee:
    def __init__(self, eid, ename, esal):
        self.eid = eid
        self.ename = ename
        self.esal = esal

    def __str__(self):
        return (self.ename)


emp = Employee(eid=12, ename="Abhi", esal=500)
print(emp)  # Only string value is returned
