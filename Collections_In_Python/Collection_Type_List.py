# Container Data Type : It ia a Entity which Contain multiple data
# It is also known as Collection Or Compound Data type
# Python Contain Following Data type = List ,Tuple, Set, Dictionaries
# A list Can Grow Or Shrink During Execution (Also Knowan As Dynamic Array)
# List is Ordered and Mutable i.e Changeable
# List is Defined in brackets []
# List Contain Dissimilar data types
# list Allows Duplicate values
# Single variable holding multiple values


# how to create a list

myList1 = [10, 20, 30, 40, 60, 70]
myList2 = ["Apple", "Banana", "Jackfruit", "cheery"]
myList3 = [10, "banana", 30, 40, "Guava", 60, 70]
myList = list()  # EmptyList

print(myList1)  # Yields [10, 20, 30, 40, 60, 70]
print(myList2)  # Yields ['Apple', 'Banana', 'Jackfruit', 'cheery']
print(myList3)  # Yields [10, 'banana', 30, 40, 'Guava', 60, 70]
print(myList)  # Yields []

# how to Access the element From A List by giving index position
myList1 = ["Apple", "Banana", "Jackfruit", "cheery"]
print(myList1[0])  # Apple
print(myList1[1])  # Banana
print(myList1[2])  # Jackfruit
print(myList1[3])  # cheery
print('**********')
# Accesing the element In Reverse Order
print(myList1[-1])  # Apple
print(myList1[-2])  # Banana
print(myList1[-3])  # Jackfruit
print(myList1[-4])  # cheery

# Accessing Element by Slice Operator/ range of Index
myList = ["Apple", "Banana", "Jackfruit", "cheery", "StrawBerry", "Kiwi", "DragonFruit"]
print(myList[2:5])  # ['Jackfruit', 'cheery', 'StrawBerry']
print(myList[2:5:2])  # ['Jackfruit', 'StrawBerry']
print(myList[-5:-2])  # ['Jackfruit', 'cheery', 'StrawBerry']

# How to change the valu in the list
myList = ["Apple", "Banana", "Jackfruit", "cheery"]
print(myList)  # ['Apple', 'Banana', 'Jackfruit', 'cheery']
myList[0] = "Orange"
myList[2] = "Mango"
print(myList)  # ['Orange', 'Banana', 'Mango', 'cheery']
myList[-1] = "Guava"
print(myList)  # ['Orange', 'Banana', 'Mango', 'Guava']

# How to read item or element of List
myList = ["Apple", "Banana", "Jackfruit", "cheery", "StrawBerry", "Kiwi", "DragonFruit"]
for i in myList:
    print(i)

# how to check whether an item is present in List or not
myList = ["Apple", "Banana", "Jackfruit", "cheery", "StrawBerry", "Kiwi", "DragonFruit"]
if "Amba" in myList:
    print("Item is present")
else:
    print("Not Present")

myList = ["Apple", "Banna", "Jackfruit", "cheery", "StrawBerry", "Kiwi", "DragonFruit"]
if "Amba" not in myList:
 print("Item is not present")
else:
 print("Is Present")


#How to count length of list
myList = ["Apple", "Banana", "Jackfruit", "cheery", "StrawBerry", "Kiwi", "DragonFruit"]
print(len(myList))

#How to add Item in to the list
myList = ["Apple", "Banana",  "DragonFruit"]
myList.append("Graps")
print(myList)#['Apple', 'Banana', 'DragonFruit', 'Grapes'] Adds the Item at last

#Adds an item as our required index Position
myList = ["Apple", "Banana",  "DragonFruit"]
myList.insert(2,"Graps")
print(myList)#['Apple', 'Banana', 'Grapes', 'DragonFruit']

#how To Remove Item from List
myList = ["Apple", "Banana", "Jackfruit", "cheery", "StrawBerry", "Kiwi"]
myList.pop(0)#['Banana', 'Jackfruit', 'cheery', 'StrawBerry', 'Kiwi'] Removed item fro zero Index
myList.pop(2)#['Banana', 'Jackfruit', 'StrawBerry', 'Kiwi'] Removed item from 2 index
print(myList)

#How to delete Item from list : Simply use del Keyword And Specify the Index Number
myList = ["Apple", "Banana", "Jackfruit", "cheery", "StrawBerry", "Kiwi"]
del myList[2]
print(myList)#['Apple', 'Banana', 'cheery', 'StrawBerry', 'Kiwi']

#How to Clear a list
myList = ["Apple", "Banana", "Jackfruit", "cheery", "StrawBerry", "Kiwi"]
myList.clear()
print(myList) # will return empty list [] ,but the list variable is present

#How to copy one list to another list
#Approach 1) By using List() method
myList1=['Apple', 'Banana', 'cheery', 'StrawBerry', 'Kiwi']
myList2=list(myList1)
print(myList1)#['Apple', 'Banana', 'cheery', 'StrawBerry', 'Kiwi']
print(myList2)#['Apple', 'Banna', 'cheery', 'StrawBerry', 'Kiwi']

#Approach 2) By using copy() Method
myList1=['Apple', 'Banana', 'cheery', 'StrawBerry', 'Kiwi']
myList2=myList1.copy()
print(myList1)#['Apple', 'Banana', 'cheery', 'StrawBerry', 'Kiwi']
print(myList2)#['Apple', 'Banana', 'cheery', 'StrawBerry', 'Kiwi']

#How to join/Combine two list
# Approach 1) by using Concatenation "+" Operator
mylist1=["A","B","C"]
mylist2=["D","E","F"]
mylist3=mylist1+mylist2
print(mylist3)#['A', 'B', 'C', 'D', 'E', 'F']

#Approach 2) by using Loop Statement
mylist1=["A","B","C"]
mylist2=["1","2","3"]
for i in mylist2:
    mylist1.append(i)
print(mylist1)#['A', 'B', 'C', '1', '2', '3']

#Approach 3) by using extend() method
mylist1=["A","B","C"]
mylist2=["1","2","3"]
mylist1.extend(mylist2)
print(mylist1)#['A', 'B', 'C', '1', '2', '3']

#Coparing Two List
mylist1=('Apple', 'Banana', 'Jackfruit', 'cheery', 'Kiwi')
mylist2=('Rice', 'Wheat', 'Rava', 'Tari', 'Mutton')

if mylist1==mylist2:
    print("Both are Same")
else:
    print("not Equal")
