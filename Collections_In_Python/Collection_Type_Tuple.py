# Tuple is Ordered and Immutable i.e Not Changeable
# Hence tuple is read only version
# If our data s fixed and never changes then we should go for tuple
# Insertion Order is preserved
# Tuple is Defined in Parenthesis () With comma Separator
# Tuple Contain Dissimilar data types
# Tuple Allows Duplicate value# Tuple is indexed based
# Single valued tuple should end with , otherwise it is not treated as tuple

# If tuple is ImmutableBelow things are not Possible
# We cannot modify existing value
# We cannot append new value
# We cannot insert a value
# We cannot remove a value


# #How to create a tuple
mytuple = ("Apple", "Banana", "Orange")

# How To create Empty Tuple
mytuple = ()

# How to Access Tuple Element(By Index Number)
mytuple = ("Apple", "Banana", "Orange")
print(mytuple[1])  # Banana
print(mytuple[-1])  # Orange

# Acessing Element By Range Of Index
mytuple = ("Apple", "Banana", "Jackfruit", "cheery", "StrawBerry", "Kiwi")
print(mytuple[::-1])  # Gives reverse Order
print(mytuple[2:5])  # ('Jackfruit', 'cheery', 'StrawBerry')
print(mytuple[-4:-2])  # ('Jackfruit', 'cheery')
print(mytuple[-2])  # StrawBerry

"""How to change a value in tuple
By default Tuple is Immutable i.e We Can't Change a value in Tuple  Once Assigned
We can Change a value in Tuple by using List approach i.e We Can Covert a Tuple into list
 mytuple-->list[mytuple]  -->tuple"""

mytuple = ("Apple", "Banana", "Jackfruit", "cheery", "Kiwi")
mylist = list(mytuple)  # Converting Tuple Into List
mylist[1] = "Orange"  # Assigning into List
print(mylist)  # ['Apple', 'Orange', 'Jackfruit', 'cheery', 'Kiwi']
mytuple = tuple(mylist)
print(mytuple)  # ['Apple', 'Orange', 'Jackfruit', 'cheery', 'Kiwi']

# Reading Elements in Tuple By Loop
mytuple = ("Apple", "Banana", "Jackfruit", "cheery", "Kiwi")
for i in mytuple:
    print(i)

# Element Checking in Tuple
mytuple = ("Apple", "Banana", "Jackfruit", "cheery", "Kiwi")
if "Banana" in mytuple:
    print("Given Item is present")
else:
    print("Given Item is not present")

# Finding the length of Tuple
mytuple = ("Apple", "Banana", "Jackfruit", "cheery", "Kiwi")
print(len(mytuple))  # 5

# Adding Element in tuple:=> Not Possible, cannot change the vale bcoz Tuple  Is Immutable
mytuple = ("Apple", "Banna", "Jackfruit", "cheery", "Kiwi")
mytuple[0] = "Orange"
print(mytuple)  # TypeError: 'tuple' object does not support item assignment

# Coping One Tuple to Another tuple: Possible coz We are not changing the value in tuple Just Coping the value
mytuple1 = ("Apple", "Banana", "Jackfruit", "cheery", "Kiwi")
mytuple2 = mytuple1
print(mytuple2)  # ('Apple', 'Banana', 'Jackfruit', 'cheery', 'Kiwi')

# Removing element From Tuple-Not Possible, cannot Remove the value bcoz Tuple  Is Immutable
mytuple = ('Apple', 'Banana', 'Jackfruit', 'cheery', 'Kiwi')
mytuple.remove("Apple")  # Invalid

# Deleting Tuple : Possible
mytuple = ('Apple', 'Banna', 'Jackfruit', 'cheery', 'Kiwi')
del mytuple
print(mytuple)

# Joining Two Tuple = Possible
mytuple1 = ('Apple', 'Banana', 'Jackfruit', 'cheery', 'Kiwi')
mytuple2 = ('Rice', 'Wheat', 'Rava', 'Tari', 'Mutton')
mytuple3 = mytuple1 + mytuple2
print(mytuple3)  # ('Apple','Banana','Jackfruit','cheery','Kiwi','Rice','Wheat','Rava','Tari','Mutton')

# Coparing Two Tupple
mytuple1 = ('Apple', 'Banana', 'Jackfruit', 'cheery', 'Kiwi')
mytuple2 = ('Rice', 'Wheat', 'Rava', 'Tari', 'Mutton')

if mytuple1 == mytuple2:
    print("Both are Same")
else:
    print("not Equal")
