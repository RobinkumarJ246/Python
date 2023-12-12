import re

mail = r'^[a-zA-z][a-zA-Z0-9]*\@+[a-zA-Z]+\.(com|in|us|net|uk)$'
mail_reg = re.compile(mail)
address = "krishnanda47@google.net"

if mail_reg.match(address):
    print("Valid address")
else:
    print("Invalid")
    
phn_reg =re.compile(pattern=r'^[0-9]{10}+$')
number = "1234567890"

if phn_reg.match(number):
    print("Valid number")
else:
    print("Invalid")