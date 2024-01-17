# Jumping statement also known as Transfer statement
# break and continue statement can be used with while and for loop based on condition
# break statements terminates the loop with out executing the else block
# continue statements skips the rest of the statement in the block and continues with the next iteration of loop

# Example for break statement
for i in range(10):
    if i == 5: # will print till 5
        break
    print(i)
print('Program executed')  # not part of block

# Example for continue statement
for i in range(10):
    if i == 5:    # will not print 5
        continue
    print(i)
print('Program executed')  # not part of block


# Example for break statement Skipping multiple value
for i in range(10):
    if i == 3 or i ==5 or i == 7: # skipping multiple value
        continue
    print(i)
print('Program executed')  # not part of block
