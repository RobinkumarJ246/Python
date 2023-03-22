#github.com/RobinKumarJ246/Python

import json
import time
import datetime
from datetime import date
from datetime import datetime, timedelta

#all datas are stored and retreived using plan.json
#set expiry date with respect to today's date(date of activation)
#time.sleep() just to bring some real effect

today = datetime.today()
new_date = today + timedelta(days=24)
expire_date = new_date.strftime('%d-%m-%Y')


print("Welcome to the portal")
time.sleep(1)

#ask user for choice
choice = int(input("Type an input\n1 for activate a plan\n2 to Deactivate a plan\n3 to Check plan details\nInput : "))
if choice == 1:
    with open('plan.json','r') as f:
        x = json.load(f)
    if x["plan"]!="active":
        amt = int(input("Enter an amount to recharge : "))
        while amt<=298 or amt >=2000:
            amt = int(input("Enter an amount between 299 and 2000 : "))
        #set the values to be changed in plan.json
        x["plan"] = "active"
        x["price"] = amt
        x["expire"] = expire_date
        with open('plan.json','w') as f:
            x = json.dump(x,f)
        print("Recharging")
        time.sleep(3)
        print("\3 Recharge successful\nExpiring on ",expire_date)
    else:
        print("You have an active plan already")

if choice == 2:
    with open('plan.json','r') as f:
        x = json.load(f)
    if x["plan"]!="deactive":
        x["plan"] = "deactive"
        x["price"] = "NULL"
        x["expire"] = "NULL"
        with open('plan.json','w') as f:
            x = json.dump(x,f)
        print("Deactivating plan")
        time.sleep(3)
        print("Plan deactivated")
    else:
        print("You have no active plans")
        
if choice == 3:
    with open('plan.json','r') as f:
        x = json.load(f)
    plan = x["plan"]
    price = x["price"]
    expire = x["expire"]
    print("Plan status : ",plan ,"\nPlan amount : ",price,"\nExpire on : ",expire)
