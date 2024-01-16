# To repeat a finite no of statement a on built Function is used called range()
# In General range(start,stop,step)
# range() Function can be used to generate sequence of Integers
# range() Function cannot be used to generate sequence of floats

for i in range(10):
    print(i)  # Generates numbers from 0 to9

for i in range(1,10):
    print(i)   # Generates numbers from 1 to9

for i in range(1,10,2):
    print(i) # Generates numbers from 1 to 9 by step 2

for i in range(20,10,-2):
    print(i)  # Generates numbers from 20 to 12 by step 2 in Reverse

print(list(range(10)))        #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(range(1,10)))      #[1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(range(10,1,-1)))   #[10, 9, 8, 7, 6, 5, 4, 3, 2]
print(list(range(1,20,2)))    #[1, 3, 5, 7, 9, 11, 13, 15, 17, 19] Prints  odd no
print(list(range(20,1,-1)))   #[20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2]



