FN = input("Enter Your First Name:")
LN = input("Enter Your Last Name:")

if FN.isupper() and LN.isupper():
    print("Good...proceed further..")
    Email = input("Enter your email:")
    if Email.islower():
        print("Good...proceed further..")
        password = input("Enter Your desries Password:")
        confirm = input("Confirm your Password:")
        if password == confirm:
            print("Good...proceed further..")
            ph_no = input("Enter your phone number:")
            if ph_no.isdigit() and len(ph_no)==10:
                print("Yay!!! your Data is submitted....!")
            else:
                print("Phone number is incorrect")
        else:
            print("Your password doesn't match...")
    else:
        print("Email error!")    
else:
    print("Name error")                