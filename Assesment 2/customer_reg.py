import re
import random
import pymysql




class customer_portal:

    Acc_no=0
    Acc_name=''
    Acc_type = ''
    mobile=0
    bal=0

    def customer_Panel(self):
        print("\t\tWelcome to Our Bank.")
        print("\t\t\tPress 1 for New customer:")
        print("\t\t\tPress 2 for Exisiting customer:")
        print("")
        customer_choice = int(input("Enter your choice 1 for New Customer & 2 for Exisiting Customer:"))
        
        if customer_choice == 1:
            self.new_customer()
        elif customer_choice == 2:
            self.database_customer_login()
        else:
            print("Wrong Input")
            return self.customer_Panels()


    def new_customer(self):
        self.Acc_no = random.randint(100000,999999)
        # Acc_no = Acc_no_rand
        self.Acc_name = input("Enter your Name: ")
        self.Acc_type = input("Type of Account- Savings or Current : ")
        self.mobile = input("Enter your mobile number: ")
        # validation
        name_val = "[A-Za-z]"
        Acc_val = "[A-Za-z]" 
        mobile_val = "[0-9]"
        x=re.findall(name_val,self.Acc_name)    
        x1=re.findall(Acc_val,self.Acc_type)
        x2=re.findall(mobile_val,self.mobile)

        try:
            if x and x1 and x2:
                if len(self.mobile)==10:
                    # self.deposit()
                    print("success")
                    print("Your Account number is : ",self.Acc_no)
                    self.operations()
                else:
                    print("mobile number invalid")
                    self.new_customer()
            else:
                print("Error! please enter valid Details ")
                self.new_customer()
        except Exception as e:
               print(e)

    def operations(self):
                print("Select the operations:")
                print("")
                print("\t\t\t1: Deposit in your Account...")
                print("\t\t\t2: Withdraw from you Account...")
                print("\t\t\t3: View Balance")
                print("")
                choice_operation = int(input("Enter your choice: "))
                
                if choice_operation == 1:
                    self.deposit()
                elif choice_operation == 2:
                    self.withdraw()
                elif choice_operation == 3:
                    self.bal()


        #  Can deposit amount 
    def deposit(self):

            Acc_deposit = int(input("Enter the amount to deposit: "))
            self.bal += Acc_deposit
            print("Your Balance is: ", self.bal)
            self.withdraw()

        #  Can Withdraw Amount 
    def withdraw(self):
            Acc_withdrawl = int(input("Enter the Amount to Withdraw: "))
            self.bal = self.bal - Acc_withdrawl
            print("Your Balance is: ", self.bal)
            self.view_balance()
    
    def view_balance(self):
            print("Your account balance is:", self.bal)
            self.Account_info()
                

        #  Can view balance         
    def Account_info(self):
            print("")
            print("Account number:", self.Acc_no)
            print("Account Name:", self.Acc_name)
            print("Account Type:", self.Acc_type)
            print("Available Bal:", self.bal)
            self.database_customer()

    def database_customer(self):
        try:
            db = pymysql.connect(host='localhost', user='root', password='', database='assessment_2')  
            print("database connected")
        except Exception as e:
            print(e)

        cr = db.cursor()
        # table_create

        tbl_create = "create table customer_info(id integer primary key auto_increment, Account_no bigint, Account_name text, Account_type text, balance bigint, mobile bigint)"

        try:
            cr.execute(tbl_create)
            print("Table created sucessfully")
        except Exception as e:
            print(e)

        insert_data = f"insert into customer_info(Account_no, Account_name, Account_type, balance, mobile)values('{self.Acc_no}','{self.Acc_name}','{self.Acc_type}','{self.bal}', '{self.mobile}')"

        try: 
            cr.execute(insert_data)
            db.commit()
            print("Data inserted sucessfully")
        except Exception as e:
            print(e)      




    Acc_no_login = 0
    deposited_amt = 0
    # Acc_name_login = input("Please enter your name:  ")
    def database_customer_login(self):
        try:
            db = pymysql.connect(host='localhost', user='root', password='', database='assessment_2')  
            print("database connected")
        except Exception as e:
            print(e)
        cr = db.cursor()

        # login_ACC_no=f"select {self.Acc_no_login} from customer_info"
        # login_ACC_name=f"select {self.Acc_name_login} from customer_info"
        self.Acc_no_login =  input("Please enter your acc no.: ")

        try:
            # login_Acc_no = f"SELECT * FROM customer_info WHERE Account_no LIKE {self.Acc_no_login}"
            login_Acc_bal = f"SELECT balance FROM customer_info WHERE Account_no LIKE {self.Acc_no_login}"
            # cr.execute(login_Acc_no)
            cr.execute(login_Acc_bal)
            login_acc_bal_det = cr.fetchall()
            print("\t", login_acc_bal_det)

            for i in login_acc_bal_det:
                 self.deposited_amt = int(i[0])
                 print("The Availabe Balance is : ",self.deposited_amt)
                 self.transactions_login()
        except Exception as e:
             print(e)
             print("no such details found!!! plz try again")
             self.database_customer_login()
    
    def transactions_login(self):
        db = pymysql.connect(host='localhost', user='root', password='', database='assessment_2')  
        cr = db.cursor()

        print("")
        print("\t\tWelcome customer")
        print("\t\tPlz check 1. for deposit")
        print("\t\tPlz check 2. for withdrawal")
        print("\t\t & 3. for exit")
        print("")
        choice_login = int(input("Enter your choice: "))
        if choice_login == 1:
            amt_to_deposit = int(input("Enter the amount to be deposited:"))
            bal = amt_to_deposit + self.deposited_amt
            print(bal)
            update_bal = f"update customer_info set balance={bal} where Account_no = {self.Acc_no_login}"
            try:
                cr.execute(update_bal)
                db.commit()
                print("Balance is updated!!!")
            except Exception as e:
                 print(e)
        elif choice_login == 2:
            amt_to_withdraw = int(input("Enter the amount to be withdrawn:"))
            if amt_to_withdraw <= self.deposited_amt:
                bal = self.deposited_amt - amt_to_withdraw
                print(bal)
                update_bal = f"update customer_info set balance={bal} where Account_no = {self.Acc_no_login}"
                try:
                    cr.execute(update_bal)
                    db.commit()
                    print("Balance is updated!!!")
                except Exception as e:
                    print(e)
            else:
                print("sorry cant proceed!!! the amout is more than deposited amount:")
                self.transactions_login()
        elif choice_login == 3:
             exit()
        else:
             self.transactions_login()

# class customer_portal(customer_register,customer_login):   
    def customer_Panel(self):
        print("\t\tWelcome to Our Bank.")
        print("\t\t\tPress 1 for New customer:")
        print("\t\t\tPress 2 for Exisiting customer:")
        print("")
        customer_choice = int(input("Enter your choice 1 for New Customer & 2 for Exisiting Customer:"))
        
        if customer_choice == 1:
            self.new_customer()
        elif customer_choice == 2:
            self.database_customer_login()
        else:
            print("Wrong Input")
            return customer_portal


# cus = customer_portal()
# cus.customer_Panel()