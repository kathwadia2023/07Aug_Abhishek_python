# Write a Python program to get the Factorial number of given number. 

n= int(input("Enter positve integer:"))
factorial = 1

if n<0:
    print("Wrong input")
elif n==0:
    print("Factorial of 0 is 1!!!")
else:
    for i in range(1, n+1):
        factorial*= i
    print(f"The Factorial value of {n} is {factorial}!!!")

