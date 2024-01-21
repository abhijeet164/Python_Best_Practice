# Arguments  / Parameters (Types Of Argument We Can Pass to the function
# 1) Positional Arguments
# 2) Keyword Arguments

# Example 1

def func(i, j):
    print(i, j)


func(2, 3)  # this will assign values to the variable as per the pre the positions  i.e i=2,j=3


def func(i, j):
    print(i, j)


func(i=20,
     j=30)  # this will assign values to the variable as we assign by key words we are not considering the position


# Example 2
def func(i, j=10):
    print(i, j)


# func(200,300)
func(200)


# EXAMPLE 3 Keywords Arguments

def greeting(greetms, name):
    print(greetms + "     " + name)


greeting(greetms="Hello", name="Abhijeet")
greeting(name="Abhijeet", greetms="Hello")  # Order Dose not Matter


# Example 4

def func(a, b, c):
    print(a, b, c)


func(10, 20, 30)  # This is positional argument
func(a=10, b=20, c=30)  # This is Keyword argument
func(b=20, a=10, c=30)  # This is Keyword argument and value is passed by changing order
func(10, 20, c=30)  # This Combination of positional argument and Keyword argument
func(10, b=20, c=30)  # This Combination of positional argument and Keyword argument


# func(10,a=20,c=30) # This Combination of positional argument and Keyword argument func(10,a=20,30) #SyntaxError:
# positional argument follows keyword argument OR we Say that positional argument must appear before keyword argument
# func(10,20,b=30) #This is not Syntax Error This is Logical Error  Note= already assigned positional value again
# Passing the keyword value for same variable


# Ex 6 A function Can return multiple values

def largest(a, b):
    if a > b:
        return a, b
    else:
        return b, a


print(largest(10, 20))
print(largest(10, 30))

res = largest(23, 42)
print(res)
