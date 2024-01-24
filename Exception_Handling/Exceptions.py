# Exception Handling ==> An unwanted and unexpected event that disturb the normal flow of program is called exception


# Ex 1  Example of Unhandled Exception
print("this is start of Program")
print("Statement 1 Executed")
print("Statement 2 Executed")
print("Statement 3 Executed")
#print(x) # NameError: name 'x' is not defined Exception Accrued
print("Statement 4 Executed")
print("Statement 5 Executed")
print("Statement 6 Executed")
print("this is end of Program")


# Ex 2 Example Of handled exception

print("this is start of Program")
print("Statement 1 Executed")
print("Statement 2 Executed")
print("Statement 3 Executed")
try:
  print(x) # Risky code placed in try block
except:
    print("Exception Occurred")
print("Statement 4 Executed")
print("Statement 5 Executed")
print("Statement 6 Executed")
print("this is end of Program")

# Ex 1
print("Program Started")
print("Program is Running")
print(10/5)
print("program is Running")
print("Program Has Ended")

# ex 2
print("Program Started")
print("Program is Running")
try:
    print(10/0)
except ZeroDivisionError :
    print("Exception handled")
print("program is Running")
print("Program Has Ended")


# Multiple Except Block
try:
    num1,num2=10,5
    result=num1/num2
    print(result)
except ZeroDivisionError:
    print(" Thrown ZeroDivisionError Exception  ")
except SyntaxError:
    print(" Thrown SyntaxError Exception  ")
except:
    print("Exception Handled")
else:
    print("No Exception Occurred")
finally:
    print("This Will Always Executed")

#Raising Our /User Defined Exception


def numberType(num):
    if num<0:
        raise ValueError("Only Integers Are Allowed")
    if num%2==0:
        print("The Number is Even")
    else:
        print(" The number is Odd")
#
numberType(20)

print("Checking Value Error Exception")
num=-1
try:
    numberType(num)
except ValueError:
    print("Value Error Exception Occurred And Handle")
print("Program Completed")
