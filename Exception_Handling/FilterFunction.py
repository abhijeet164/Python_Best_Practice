# The filter() Function Returns an Iterator where the items are filtered through a function to Test ig the item is
# accepted or not

# Ex 1) Filter Function Without using Lambada Function

ages = [5, 12, 25, 18, 16, 32, 24]


def myFunc(x):
    if x < 18:
        print("the value is false", x)
        return False
    else:
        print("The Value is True", x)
        return True


adult = list(filter(myFunc, ages))
for x in adult:
    print(x)

# Ex 2 Filter() Function with Lambada Expression

ages = [5, 12, 25, 18, 16, 32, 24]

adult = filter(lambda a: a > 18, ages)
for x in adult:
    print(x)
