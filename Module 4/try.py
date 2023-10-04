# Write python program that user to enter only odd numbers, else will raise an exception. 
x = int(input("Enter odd number:")) 

try:
    if x%2!=0:
        print("ODD number")
    
except:
    while x%2==0:
        print("Even number")
        x = int(input("Enter odd number:"))
    # print("odd number entered...")
    print("Odd number") 


