'''Write a Python program to add 'ing' at the end of a given string 
(length should be at least 3). If the given string already ends with 'ing'
then add 'ly' instead if the string length of the given string is less than 3, leave it unchanged.  '''

str = input("Enter word:")

if len(str)>2:
    if str[-3:]!= 'ing':
        str+='ing'
        print(str)
    elif str[-3:]== 'ing':
        str += 'ly'
        print(str)
    # print("done")
else:
    print(str)