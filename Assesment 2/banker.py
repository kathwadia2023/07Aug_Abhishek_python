import pymysql
import re
# from customer_reg import *
# Baker Module
# Banker 


class Banker:
#  Can Register 

    banker_username=""
    banker_password=''

# bakers choice nw reg or existing
    def choice(self):
        print("")
        print("Welcome to Banker side portal!")
        choice_banker = int(input("Enter the choice : new registration[1] and exisiting[2]: \n"))
        if choice_banker == 1:
            self.banker_register()
        elif choice_banker == 2:
            self.login()
        else:
            print("wrong input")
            self.choice()

# banker's registration
    def banker_register(self):
        
        self.banker_username= input("Please Enter a username to register:\n")
        self.banker_password = input("Please Enter password [must have min 6 to max 12 characters]:\n")
        

        password_val = "[A-Za-z0-9@#$!_]+[A-Za-z0-9@#$!_]{2,4}+[A-Za-z0-9@#$!_]+[A-Za-z0-9@#$!_]"
        x = re.findall(password_val,self.banker_password) 
        if x:
            if 8<=len(self.banker_password)<=14:
                print("Password is Valid")
                c_password = input("Confirm your password: ")
                if c_password == self.banker_password:
                    print("Your password is valid")
                    self.banker_db()
                    self.customer_banker_operation()
                else:
                    print("Invalid password")
                    self.banker_register()
            else:
                print("invalid password")
                self.banker_register()



#  banker's databse
    def banker_db(self):
        try:
            db = pymysql.connect(host='localhost', user='root', password='', database='assessment_2')  
            print("database connected")
        except Exception as e:
            print(e)

        cr = db.cursor()
        # table_create

        tbl_create = "create table banker_info(id integer primary key auto_increment, banker_name text, password varchar(20))"

        try:
            cr.execute(tbl_create)
            print("Banker Table created sucessfully")
        except Exception as e:
            print(e)

        banker_insert_data = f"insert into banker_info(banker_name, password)values('{self.banker_username}','{self.banker_password}')"

        try: 
            cr.execute(banker_insert_data)
            db.commit()
            print("Data inserted sucessfully")
        except Exception as e:
            print(e)      


# banker's login
    def login(self):
        self.log_username = input("Enter your Name: ")
        self.log_pass = input("Enter your password: ")


        try:
            db = pymysql.connect(host='localhost', user='root', password='', database='assessment_2')  
            print("database connected")
            cr = db.cursor()        
            # login_user_db = f"SELECT * FROM `banker_info` WHERE banker_name={self.log_username}"
            login_pswd_db = f"SELECT * FROM banker_info WHERE banker_name='{self.log_username}' and password='{self.log_pass}'"
            # SELECT balance FROM customer_info WHERE Account_no LIKE {self.Acc_no_login}
            try:    
                # cr.execute(login_user_db)
                cr.execute(login_pswd_db)
                print("Validtated Sucessfully")
                self.customer_banker_operation()
            except Exception as e:
                print(e)
                print("Invalid credentials...")
                self.login()
                
        except Exception as e:
            print(e)




# customer operation
#  Can Update all Customers
#  Can View all Customers
#  Can Delete all Customers
    def customer_banker_operation(self):
        print("Enter your choice regarding Customer")
        print("")
        print("\t \t Press 1 for viewing all customer details")
        print("\t \t Press 2 for upadating a customer's detail")
        print("\t \t Press 3 for deleting a customer details")
        print("")
        choice_banker_operation = int(input("Enter your choice: "))
        
        if choice_banker_operation ==1:
            view_all = "SELECT * FROM `customer_info`"

            try:
                db = pymysql.connect(host='localhost', user='root', password='', database='assessment_2')  
                print("database connected")
                cr = db.cursor()
                cr.execute(view_all)
                data = cr.fetchall()
                print(data)        
            except Exception as e:
                print(e)
                print("try again")
                self.customer_banker_operation()

        elif choice_banker_operation ==2:
            self.cust_name = input("Enter the name of customer to be rectified: ")
            self.cust_new_name = input("Enter new name: ")
            #  = f"select Account_name from customer_info  "
            update_customer_detail= f"update customer_info set Account_name='{self.cust_new_name}' where Account_name='{self.cust_name}'"
            try:
                db = pymysql.connect(host='localhost', user='root', password='', database='assessment_2')  
                print("database connected")
                cr = db.cursor()
                cr.execute(update_customer_detail)
                db.commit()
                print("Customer name is updated")        
            except Exception as e:
                print(e)
                print("try again")
                self.customer_banker_operation()
        elif choice_banker_operation ==3:
            self.cus_del_name = input("Enter the name of customer for deleting account details: ")
            delete_customer_detail= f"delete from customer_info where Account_name='{self.cus_del_name}'"
            try:
                db = pymysql.connect(host='localhost', user='root', password='', database='assessment_2')  
                print("database connected")
                cr = db.cursor()
                cr.execute(delete_customer_detail)
                db.commit()
                print("Record is deleted")        
            except Exception as e:
                print(e)
                print("try again")
                self.customer_banker_operation()
        else:
            self.customer_banker_operation()




# bank = Banker()
# bank.choice()   
