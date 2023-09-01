#  Write a Python function to reverses a string if its length is a multiple of 4.  

str = input("Enter gibberish:")
# "this is python and we are glad to be learning it"

if len(str)%4==0:
    print(str[::-1])
else:
    print("not a muliple of 4")
    