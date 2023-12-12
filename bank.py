import time
import json
print('Welcome to the bank portal')

with open('data.json','r') as f:
    x = json.load(f)
acc_if = x['acc']
if acc_if == "0":
    print("Create your account now")
    name=input("Enter an username : ")
    password=input("Set a password : ")

    with open('data.json','r') as f:
        x = json.load(f)
    
    x['name'] = name
    x['password'] = password
    x['acc'] = "1"
    
    with open('data.json','w') as f:
        x = json.dump(x,f)
    print("Account created successfully")
    
else:
    print("Login to your account")
    logname=input("ENTER YOUR USERNAME : ")
    logpassword=input("ENTER YOUR PASSWORD : ")
    bal = x['balance']
    print("Logging you in")
    
    time.sleep(3)
    with open('data.json','r') as f:
        x = json.load(f)
    if x['password'] != logpassword:
        print("Incorrect password\nConnection timed out")
    else:
        time.sleep(4)
        print("Successfully logged in")
        time.sleep(2)
        choice=int(input("Select an option\1.Check balance\n2.Withdraw amount\n3.Deposit amount\n Enter choice : "))
        with open('data.json','r') as f:
            x = json.load(f)
        if choice==1:
            print(bal)
        elif choice ==2:
            withamt=int(input("Enter amount : "))
            if withamt <= bal:
                print("Successfully withdrawn")
                bal = bal - withamt
                with open('data.json','r') as f:
                    x = json.load(f)
                    x['balance'] = bal
            else:
                print("Insuffient balance")
    
                with open('data.json','w') as f:
                    x = json.dump(x,f)
        elif choice ==3:
            depamt=int(input("Enter amount : "))
            print("Successfully deposited")
            bal = bal + depamt
            with open('data.json','r') as f:
                x = json.load(f)
                x['balance'] = bal
    
            with open('data.json','w') as f:
                x = json.dump(x,f)
        else:
            print("Connection timed out")