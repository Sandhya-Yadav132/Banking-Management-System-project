
# import time 

#-------------------------Banking Management System----------------------

admin_account={
    2001:{'name':'Alban',
          'password':'Alban@123',
          'role':'admin',
          'mobile_number':95447555145,
          'dob':'20-4-2002',
          },

    # 2002: ("Sandhya", "sdgfs234#", "Admin", "", "")  #do not use because of well defined structure
          
}
# name = admin_account[2002][0] # Sandhya

accounts={
   1001:{'name':'Alban',
          'password':'Alban@123',
          'role':'admin',
          'mobile_number':95447555145,
          'dob':'20-4-2002',
          },
   1002:{ "name":"Sandhya Yadav",
         'username':'sandhya132',
        'password':"Sandhya@123",
        'balance':0.0,
        'mobile_number':9544752117,
        'dob':'26-8-2004',
        'role':'user'},
   1003:{ "name":"Krishna Karma",
        'username':'kanha123',
        'password':"Kanha@123",
        'balance':0.0,
        'mobile_number':9544752677,
        'dob':'08-09-2004',
        'role':'user'},
   1004:{'name':'Harsh',
          'password':'Harsh@123',
          'role':'admin',
          'mobile_number':95447555145,
          'dob':'21-06-2004',
          },
    1005:{'name':'Tulja',
          'username':'tulja184',
          'password':'Tuija@123',
          'balance':0.0,
          'role':'user',
          'mobile_number':95447555145,
          'dob':'18-04-2003',
          } 
}


def search_user():
     while True:
        user_id=int(input("Search User by UserId of user : "))
        if user_id in accounts and accounts[user_id]['role']=='user':
            view_account(user_id)
            break
        else:
            print("User does not exist")

def view_all_account():
     print(f"\n    ** All User accounts**   \n")
     for k in accounts.keys():
          if accounts[k]['role']=='user':     
               print(f"UserID : {k}\n"
                    f"Name : {accounts[k]['name']}\n"
                    f"Balance : {accounts[k].get('balance',0.0)}\n"
                    f"Mobile Number : {accounts[k].get('mobile_number','N/A')}\n"
                    f"Date of Birth : {accounts[k]['dob']}\n"
                    )
          else:
              continue
           
# view_all_account()

def admin_menu(user_id='Admin'):
    # print(f"\n     **Admin panel : Welcome {admin_account[user_id]['name']}!**")

    while True:
        print(f"\n     **Admin panel : Welcome {accounts[user_id]['name']}!**")
        print('''
1. View All account details
2. Search User account
3. Logout'''
        )
        choice=input("Please Enter your choice : ")
        match choice:
            case '1':
                view_all_account()
            case '2':
                search_user()
            case '3':
                print("Logged out!")
                break
            case _:
                print("Invalid choice")

def view_account(user_id):
     print(f'\n  **Account details**')
     print(
          f'UserID : {user_id}\n'
          f'Name : {accounts[user_id]['name']}\n'
          f'Balance : ₹ {accounts[user_id]['balance']}\n'
          f'Mo. Number : {accounts[user_id].get('mobile_number','N/A')}\n'
          f'Date of birth : {accounts[user_id].get('dob','N/A')}\n'
     )
     
# view_account(1002)           
     
def check_balance(user_id):
     print(f'\n    Balance Check Succesfully\n'
           f'Available balance : ₹ {accounts[user_id]['balance']}\n'
     )

def deposit(user_id):
     total_amount=accounts[user_id]['balance']
     while True:
        amount=input("Enter amount : ")
        if amount.isdigit() and int(amount)>0:
            total_amount+=int(amount)
            accounts[user_id]['balance']=total_amount
            print("Deposit succesfully\n")
            break
        else:
            print('Please Enter valid amount')

def withdraw(user_id):
    total_amount=accounts[user_id]['balance']
    while True:
        amount=input("Enter amount : ")
        if amount.isdigit() and int(amount)>0:
            if int(amount)<=total_amount:
                total_amount-=int(amount)
                accounts[user_id]['balance']=total_amount
                print("withdraw succesfully\n")
                break
            else:
                print("Insufficient balance ")
                break
        else:
            print('Please Enter valid amount')

def user_menu(user_id='User'):
    while True:
        print(f"\n     **User Panel : Welcome {accounts[user_id]['name']}!**")
        print('''
1. View own account details
2. Check Balance
3. Deposit
4. Withdraw
5. Logout'''
        )
        choice=input("Please Enter your choice :")
        match choice:
            case '1':
                view_account(user_id)
            case '2':
               check_balance(user_id)
            case '3':
                deposit(user_id)
            case '4':
                withdraw(user_id)
            case '5':
                print("Logged out!")
                break
            case _:
                  print("Invalid choice")
                              
def user_login():
    # compare role based in same table
    while True:
        user_id=input("Enter UniqueID : ")
        if user_id.isdigit():
            user_id=int(user_id)
            break
        else:
            print("Invalid input")
    if user_id in accounts and accounts[user_id]['role']=='user':
        attempts=0
        while attempts<3:
            password=input("Password : ")
            if password==accounts[user_id]['password']:
                print("Login Succesfully! ")
                user_menu(user_id)
                break
            else: 
                print("Incorrect Password ")
                attempts+=1  
    else:
        print("User not found")     

# user_login()

def admin_login():
    # compare role based in same table
     while True:
        user_id=input("Enter UniqueID : ")
        if user_id.isdigit():
            user_id=int(user_id)
            break
        else:
            print("Invalid input")
     if user_id in accounts and accounts[user_id]['role']=='admin':
        attempts=0
        while attempts<3:
            password=input("Password : ")
            if password==accounts[user_id]['password']:
                print("Login Succesfully! ")
                admin_menu(user_id)
                break
            else: 
                print("Incorrect Password ")
                attempts+=1  
     else:
        print("Admin not found")
  
def create_account():
    # Automatically key increment
    if accounts:
        new_id= max(accounts.keys()) + 1
    else: 
        new_id=1001
    
    # User's name
    while True:
        name=input("Full name : ").title()
        if len(name)==0:
            print("Required Field")
        elif name.isalnum() or len(name)>30:   # space between the characters
            print("Please enter valid name ") 
        else:
            break
    
    # user's username
    while True:
            user_name=input("Username : ")
            num=('0','1','2','3','4','5','6','7','8','9')
            if len(user_name)==0:
                break
            elif len(user_name)<10 or user_name.startswith(num):
                print("Please enter valid username,it must contain at least 10 characters ,1 number") 
            else:
                break
            

    # password validations 
    while True:
        password=input("Password : ")
        if len(password)==0:
            print("Required Field")
        elif len(password)<8 or not password.isalnum() or not password.istitle():
             print("Password must contain at least 8 characters, 1 uppercase letter, 1 number, and 1 special symbol.")
        else:
           break
       
    # mobile number validations   
    while True:
        mobile_number=input("Mobile Number : ")
        if len(mobile_number)==0:
            break
        elif 10<=len(mobile_number)<=10 and mobile_number.startswith(('6', '7', '8', '9')):
            break
        else:
            print("Please enter valid number ")
    
    # date of birth validations
    while True:
        dd,mm,yy=map(str,input("Date Of Birth (DD/MM/YYYY) : ").split('/'))
        if len(dd)<=2 and len(mm)<=2 and len(yy)==4:
            dob=dd.zfill(2)+'-'+mm.zfill(2)+'-'+yy
            break
        else:
            print("Enter valid Date of birth ")
    
    # new user update in available dictionary 'accounts'    
    accounts[new_id]={
        'name':name,
        'username':user_name,
        'password':password,
        'balance':0.0,
        'mobile_number':mobile_number,
        'dob':dob,
        'role':'user'
        }
    print(f"Your account created succesfully!\nYour UserID is {new_id}")

create_account()

def main_menu():
    while True:
        print('\n------Banking Management System---------------')
        print('''
1. Create User Account
2. Login as a Admin
3. Login as a User
4. Exit '''
        )

        choice=input("Please choose an option : ")
        match choice:
            case "1":
                create_account()
            case "2":
                admin_login()
            case "3":
                user_login()
            case "4":
                print("Thank You! ")
                break
            case _:
                print("Invalid choice ")
    
# main_menu()  # main control
















def login():
    # separated tables/dict
    user_id =int(input("Enter UserID : "))
    if user_id in accounts:
        data=accounts
    elif user_id in admin_account:
        data=admin_account
    else:
        print("Account does not exist")
        attempts=0
        while attempts<3:
            password=input("Password : ")
            if password==data[user_id]['password']:
                print("Login Succesfully! ")
                if data[user_id]['role']=='user':
                    user_menu(user_id)
                    break
                else:
                    admin_menu(user_id)
                    break
            else: 
                print("Incorrect Password ")
                attempts+=1
  
def login_validation(user_id):   
        if user_id in accounts:     
        # maximum 3 attempts for password verification    
            attempts=0
            while attempts<3:
                password=input("Password : ")
                if password==accounts[user_id]['password']:
                    print("Login Succesfully! ")
                    if  accounts[user_id]['role']=='user':
                        user_menu(user_id)
                        break
                    else:  
                        admin_menu(user_id)
                        break
                else: 
                    print("Incorrect Password ")
                    attempts+=1
        else:
            print("Account does not exist")

def edit_profile(user_id):
    if accounts[user_id]['role']=='user':
                    while True:
                        choice = input("If you want to edit your account details \n1.Yes \n2.No\nChoose : ")
                        match choice:
                            case '1':
                                # while True:
                                #     mobile_number=input("Mobile Number : ")
                                #     if 10<=len(mobile_number)<=10 and mobile_number.startswith(('6', '7', '8', '9')):
                                #         accounts[user_id]['mobile_number']=mobile_number
                                #         continue
                                #     else:
                                #         print("Please enter valid number ")

                                   
                                #     new_password=input("Password : ")
                                #     if len(new_password)>8 and new_password.isalnum() and new_password.istitle():
                                #         print("hi")
                                #         break
                                #     else:
                                #         print("Password must contain at least 8 characters, 1 uppercase letter, 1 number, and 1 special symbol.")
                                print('hi')
                            case '2':
                                break
                            case _:
                                print("Invalid choice")

# edit_profile(1002)

def view_all_admin():
     print(f"\n    ** All Admin Details**   \n")
     for k in accounts.keys():
          if accounts[k]['role']=='user':     
              continue
          else:
              print(f"UniqueID : {k}\n"
                  f"Name : {accounts[k]['name']}\n"
                  f"Mobile Number : {accounts[k]['mobile_number']}\n"
                  f"Date of Birth : {accounts[k]['dob']}\n"
             )
            
# view_all_admin()


# id=input("Enter UniqueID : ")
# user_id=int(id)
# print(user_id)
# print(type(user_id))
# print(type(id))

# print('sa ndhya '.strip()) #sa ndhya


while True:
        user_id=input("Enter UniqueID : ")
        if user_id.isdigit():
            user_id=int(user_id)
            break
        elif user_id.isalnum() or user_id.isalpha():
            username=user_id
            break
        else:
            print("Invalid input")
if  user_id in accounts and accounts[user_id]['role']=='user':
        attempts=0
        while attempts<3:
            password=input("Password : ")
            if password==accounts[user_id]['password']:
                print("Login Succesfully! ")
                user_menu(user_id)
                break
            else: 
                print("Incorrect Password ")
                attempts+=1  
else:
        print("User not found")     
