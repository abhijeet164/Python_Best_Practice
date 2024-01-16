# Conditional Statement OR Decision Control Statement
# Three Ways For Taking decision in Program = if,if else,elif

# Syntax for if
# if condition:
#        statement1
#        statement2

# Syntax for if else
# if condition:
#        statement1
#        statement2
# else:
#     statement1
#     statement2

# Syntax for  elif :When we need to Verify Multiple conditions
# if condition1:
#        statement1
#        statement2
# elif condition2:
#        statement3
# elif condition3:
#        statement4


# Example No 1 Check Eligibility to Vote
age = int(input("Please Enter Your Age "))
if age >=18:
    print("Eligible for Vote")
else:
    print("Not Eligible for Vote")

# Example no 2 To Check Even Or Odd
num = int(input("Enter a Number"))
if num%2==0:
    print("Given Number is Even")
else:
    print("Given Number is Odd")

# Example no 2 To Check Even Or Odd approach 2 in Single Line (ternary Operator)
print("Given Number is Even") if num%2 ==0 else print("Given Number is Odd")

# EXample no 2.1 Multiple Statement In Singile Line
a =20
{print('Hello'),print('Python')} if a >=10 else {print('hi'),print('Java')}

# Example For elif

weekday = 1
if weekday ==1 :
    print('Sunday')
elif weekday == 2:
    print('Monday')
elif weekday == 3:
    print('Tuesday')
elif weekday == 4:
    print('Wednesday')
elif weekday == 5:
    print('Thrusday')
elif weekday == 6:
    print('Friday')
elif weekday == 7:
    print('Saturday')
else:
    print('Invalid Input')





































