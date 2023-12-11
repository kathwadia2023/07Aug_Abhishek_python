# A program for Banking Application
from banker import *
from customer_reg import *




cus = customer_portal()
banker = Banker()

def choice_operation():

    Y_or_N='Y'
    while Y_or_N != 'N':
        print("\tWelcome to the Banking Applications")
        print("")
        print("\t\t Press 1 for Banker")
        print("\t\t Press 2 for Customer")
        print("\t\t Press 3 for Exit!")
        print("")


        choice = int(input("Plz Enter your Choice [Banker:1] or [Customer:2]: "))
        if choice == 1:

            
            banker.choice()
            Y_or_N = input("Want to continue : Y or N : ")
            if Y_or_N == 'Y':
                choice_operation()
            else:
                exit()

        elif choice == 2:
            # cus.customer_Panel()
            cus.customer_Panel()
            Y_or_N = input("Want to continue : Y or N : ")
            if Y_or_N == 'Y':
                choice_operation()
            else:
                exit()

        elif choice ==3:
            exit()
        else:
            print('Wrong choice try again!!!')
            exit()

    
        # Y_or_N = input("Want to continue : Y or N : ")
        # if Y_or_N == 'Y':
        #     choice_operation()
        # else:
        #     exit()

choice_operation()