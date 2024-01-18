# How To create a Dictionary  mydict={Key:Value}

mydict = {101: "Abhi", 102: "Vishu", 103: "Shruti", 104: "Amar"}
print(mydict)  # 101: 'Abhi', 102: 'Vishu', 103: 'Shruti', 104: 'Amar'} And also not maintain the order internally
print(type(mydict))  # <class 'dict'>

# How to Acess the Elements from Dictionary
# Call By key
mydict = {
    "Brand": "maruti",
    "Model": "i10",
    "year": 2021
}
print(mydict["Brand"])  # maruti Key will Return Value
# By get() Method
x = mydict.get("Model")
print(x)  # i10

# How to change Values (**Not Key coz they are unique) in Dictionary

mydict = {

    "Brand": "maruti",
    "Model": "i10",
    "year": 2021
}
print(mydict)  # without change={'Brand': 'maruti', 'Model': 'i10', 'year': 2021}
mydict["year"] = 2022  # Adding new value
print(mydict)  # with change=>{'Brand': 'maruti', 'Model': 'i10', 'year': 2022}

# How to read values in Set
mydict = {

    "Brand": "maruti",
    "Model": "i10",
    "year": 2021
}

# Approach = 1)
for i in mydict:
    print(i)  # prints only key from dictionary

# Approach = 2)
for i in mydict:
    print(mydict[i])  # prints values from dictionary

# Approach = 3)
for i in mydict.values():
    print(i)

for i in mydict.keys():
    print(i)
# Approach = 4) prints both key and value
for x, y in mydict.items():
    print(x, y)

# How to Check existance of key in dictionary
mydict = {

    "Brand": "maruti",
    "Model": "i10",
    "year": 2021
}
if "Braxnd" in mydict:
    print("Given Key Exist")
else:
    print("Given Key Does Not Exist")

# for getting Boolean Value
print("Brand" in mydict)

# How to check total no of Items in Dectionary
mydict = {

    "Brand": "maruti",
    "Model": "i10",
    "year": 2021
}
print(len(mydict))  # 3

# Adding items in Dictionary
mydict = {"Brand": "maruti", "Model": "i10", "year": 2021, "Colour": "Red"}
print(mydict)  # {'Brand': 'maruti', 'Model': 'i10', 'year': 2021, 'Colour': 'Red'}

# Remove Item from Dictionary
mydict = {

    "Brand": "maruti",
    "Model": "i10",
    "Year": 2021
}
# mydict.pop("Year")
print(mydict)  # {'Brand': 'maruti', 'Model': 'i10'}
del mydict["Model"]
print(mydict)  # {'Brand': 'maruti', 'Year': 2021}
# del mydict  # Deletes  dict
mydict.clear  # Clears only element/item And Variable is Present

# Coping one dict into another dict without copy() Function
mydict = {

    "Brand": "maruti",
    "Model": "i10",
    "year": 2021
}
mydict1 = mydict
print(mydict1)  # {'Brand': 'maruti', 'Model': 'i10', 'year': 2021}

# Using Copy Function
mydict1 = mydict.copy()
print(mydict1)  # {'Brand': 'maruti', 'Model': 'i10', 'year': 2021}
