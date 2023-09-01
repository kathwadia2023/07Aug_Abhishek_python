# Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string.
#  If the string length is less than 2, return instead of the empty string.  

str = input("Enter your string:")
# "This is python! and it is amazing!!!"

if len(str)>2: 
    new_str = str[0:2] + str[-2:]
    print(new_str)
else:
    print("The string is empty")

