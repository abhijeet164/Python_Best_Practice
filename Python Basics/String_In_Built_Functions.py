# Creating String Variable And Assign Value
# <Variable Name> = <Collections of Unicode Character>
# string Properties
# Python Strings are immutable - They cannot be changed
# String Can be Concatenated using '+'


# Ways of Creating String

s = 'Welcome'  # In Single quotes
s = "Welcome"  # In Double quotes
s = str('welcome')  # In Single quotes
s = str("welcome")  # In Double quotes

# Creating empty Strings Variables
name = ''
name = ''
name = str('')

# Effect of Operators on Sting
str1 = 'Welcome'
print(str1 + 'Abhijeet')  # Will Yield Concatenation = WelcomeAbhijeet
print(str1 * 2)  # Will Yield 2 times o/p at console = WelcomeWelcome

# Accessing String elements
str_A = 'Abhijeet Rane'
print(str_A[0])  # Yields A
print(str_A[1])  # Yields b
print(str_A[2])  # Yields h
print(str_A[3])  # Yields i
print(str_A[4])  # Yields j
print(str_A[5])  # Yields e

# Acessing String elements in Reverse Order
print(str_A[-5])  # Yields R
print(str_A[-4])  # Yields  a
print(str_A[-3])  # Yields n
print(str_A[-2])  # Yields e
print(str_A[-1])  # Yields (Space)

# Accessing Sub_String of a String
str_A = 'Abhijeet Rane'
print(str_A[1:5])  # Extract from Specified value of Index Position => bhij
print(str_A[:5])
print(str_A[1:3])
print(str_A[-5:-1])
print('Sclicinhg of String')

#ord() and chr() Returns ASCII Value and viceversa
print(ord('A')) #==>65
print(chr(65))  #==> A

#prints min() , max() ,len()
print(min('abc'))  #a
print(max('abc'))  #c
print(len('abhijeet')) #8

#MebershipOperator : in & not in Operator
str1="Welcome to pune"
print("come" in str1) #if there returns boolean value == True
print("Wel"in str1)#True
print("abhi"not in str1)#True
print("pune" not in str1) #False

#String Comparison  : compares on alphabetical Order
print("tim"== "tie") #False
print("free"!= "freedom") #True
print("arrow">"arron") #True
print("abhi"<"abhijeet") #True
print("right">="left") #True
print("Yellow"<="fellow") #True
print("abc">"") #False


# Testing String OR Type of Character present in String
s="Welcome To Kolhapur"
print(s.isalnum())
print(s.isalpha())
print(s.isascii())

# finding Substring  Returns Boolean Value
st = "Welcome to pune"
print(st.endswith("w"))
print(st.endswith("e"))
print(st.startswith("welcome"))
print(st.startswith("to"))
