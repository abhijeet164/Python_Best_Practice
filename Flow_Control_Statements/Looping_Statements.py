# Looping Statements OR Repetition Control Statement
# It Helps to repeat a set of Statement in Progra
# There are Two Types of Looping Statements OR Repetition Control = 1) while 2) for
# There is no do-while in Python

# Syntax For Whole loop
# 1.Initialization :Staring Point,2.Condition: When to Stop 3.Increment : Till what Range
# while condition:
#       statement1
#       statement2

# Print 1 to 10 Numbers
i = 1  # initialization
while i <= 10:  # Condition
    print(i)
    i = i + 1  # Increment
print('Executed Successfully')

# Print 1 to 10 Numbers in Descending Order
i = 10  # initialization
while i >= 1:  # Condition
    print(i)
    i = i - 1  # Increment
print('Executed Successfully')

# For Loop : For loop is used to itrate over sequqnce Such as String Tuple or list
# Syntax : for var in list:
#           statement1
#           statement2

# Ex 1
for i in range(11):
    print(i)

# Ex 2
for i in range(1,10,2):
    print(i) # prints odd no 1 to 10


# Ex 3 Prints even no
for i in range(0,21,2):
    print(i)