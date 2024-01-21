# Golabal variable : Variable out Side the function
# Local Variable : Variable  are inside the function or method

global_Var = 20  # Golabal variable


def func():
    local_var = 10  # Local Variable
    print(local_var)
    print(global_Var)


func()

# print(local_var) # Cant Access / invalid
print(global_Var)  # Valid

# Ex 2
xy = 200  # Global var


def cool():
    xy = 100  # Local VAr
    print(xy)


cool()
print(xy)

# Ex 3 Accessing the  the global variable(IF HAving same name) inside a Function Or Method
# just use global keyword for accessing
xy = 100  # Global var


def cool():
    global xy
    xy = 200  # Access Global Variable And Modify the value by using global key word
    print(xy)


cool()
print(xy)  # 200mThe vale of global is modified

# Ex 4
xy = 100  # Global var


def cool():
    global xy
    xy = 200  # Access Global Variable And Modify the value by using global key word
    print(xy)


print(xy)  # 100  In this Example We Have Note Called the Function So It Wont update the value of Global Variable


# Ex 5  We Can Declare a global variable inside a function
def cool():
    global xy
    xy = 200  # Access Global Variable And Modify the value by using global key word
    print(xy)


cool()  # 200
print(xy)  # 200 We Can Access the Global variable  any where
