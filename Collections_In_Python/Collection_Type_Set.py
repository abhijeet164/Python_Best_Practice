# if we want to represent a group of of unique values as a single entity than we should go for set
# Duplicates are not allowed
# insertion order is not preserved .But we can sort the Elements
# Indexing and slicing is not allowed for set
# Set object are mutable
# defined i Curly braces {} with comma separation
# Can apply Mathematical Operation like Union ,Intersection,difference,etc on set

# How To Create A Set :

# 1) Empty Set
mySet = {}

# How to Access A Set Elements: We Cant use Index Position As it doesn't Follow Insertion Order
mySet = {"Apple", "Banana", "Grapes", "Kiwi", "Orange"}
for i in mySet:
    print(i)

# How to Check Whether A value  Exit Or Not
# Approach 1)
mySet = {"Apple", "Banana", "Grapes", "Kiwi", "Orange"}
if "Apple" in mySet:
    print("The Given Element Is Present")
else:
    print("The Given Element Does not Exit")

# Approach 2)
mySet = {"Apple", "Banana", "Grapes", "Kiwi", "Orange"}
print("Apple" in mySet)  # True
print("Chiku" in mySet)  # False

# Adding Elements To Set
"""We can Add Values/Elements to Set By :=> 1)add()    2) update()
add() :=> When we want to add a Single Item than we can go for add() Method/Function
Update :=> When we want to add Multiple Item / Element to Set we go for update()  Method/Function"""

# For Single Value
mySet = {"Apple", "Banana", "Grapes", "Kiwi", "Orange"}
mySet.add("DragonFruit")
print(mySet)  # {'Kiwi', 'Grapes', 'Orange', 'Banana', 'Apple', 'DragonFruit'}

# For Multiple Value
mySet = {"Apple", "Banana", "Grapes", "Kiwi", "Orange"}
mySet.update(["DragonFruit", "Chiku", "Ratali", 10, 20, 11.5])  # Heterogeneous Data Is Allowed
print(mySet)  # {'Ratali', 10, 11.5, 'DragoanFruit', 20, 'Chiku', 'Kiwi', 'Grapes', 'Orange', 'Apple', 'Bannana'}

# Finding Length of Set
mySet = {"Apple", "Banana", "Grapes", "Kiwi", "Orange"}
print(len(mySet))  # 5

# How to remove Item from Set:=> 1)remove() & 2) discard()
mySet = {"Apple", "Banana", "Grapes", "Kiwi", "Orange"}
mySet.remove("Apple")
print(mySet)  # {'Kiwi', 'Orange', 'Banana', 'Grapes'}
mySet.remove("xzr")  # KeyError: 'xzr' Whenever trying to remove an Element Which is Not Present in the Set will
# give An error

# 2) discard() method
mySet = {"Apple", "Banana", "Grapes", "Kiwi", "Orange"}
mySet.discard("Kiwi")
print(mySet)  # {'Apple', 'Orange', 'Banana', 'Grapes'}
mySet.discard("XYZ")  # in discard it will not give you and Error if we are giving an element which is not present
# in  set ..
# This is the only difference in remove() and discard

# How to Clear all items in Set
mySet = {'Apple', 'Orange', 'Banana', 'Grapes'}
mySet.clear()
print(mySet)  # Returns An Empty Set

# How To delete a Set
mySet = {'Apple', 'Orange', 'Banana', 'Grapes'}
del mySet
print(mySet)  # NameError: name 'mySet' is not defined Becoz Already Deleted

# how To join two Set  1) Union 2)update
set1 = {"A", "B", "C"}
set2 = {1, 2, 3, 4}
set3 = set1.union(set2)  # We Cannot use Concatenation
print(set3)  # {1, 2, 'A', 3, 'C', 4, 'B'} Order will Not Be Maintained

# By update() function
set1 = {"A", "B", "C"}
set2 = {1, 2, 3, 4}
set1.update(set2)
print(set1)  # {'B', 1, 2, 3, 4, 'A', 'C'}
