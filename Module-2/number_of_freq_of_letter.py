# Write a Python program to count the number of characters (character frequency) in a string  

str1=input("Enter your Statement:")

for i in str1:
    frequency = str1.count(i)
    
    print(str(i) + ": " + str(frequency)) 