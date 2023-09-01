#======== Write a python program to sum of the first n positive integers.
n = int(input("Enter N:"))
sum = 0

if n<1:
    print("The entered value is not a natural number...")
else:
    for i in range (n+1):
        sum += i
        
print(f"the sum is: ",sum)