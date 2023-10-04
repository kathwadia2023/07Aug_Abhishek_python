# Write python program that user to enter only odd numbers, else will raise an exception. 
x = int(input("Enter odd number:")) 

try:
    while x%2==0:
        print("Even number")
        x = int(input("Enter odd number:"))
    # print("odd number entered...")
except:
    print("Odd number") 


