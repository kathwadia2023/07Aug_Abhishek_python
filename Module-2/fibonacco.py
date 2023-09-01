# Write a Python program to get the Fibonacci series of given range. 



n = int(input("Enter positive integer:"))
a = 0
b = 1
c = a + b
i = 1
print("Fibonacci series is: ")
while i<=n:
	i+=1
	print(a)
	a = b
	b = c
	c = a + b



	