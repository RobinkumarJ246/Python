def prime(num):
    count = 0
    for i in range(1,num):
        if num%i==0:
            count = count+1
    if count>2:
        return False
    else:
        return True

num = 5
if prime(num)==True:
    print("{} is a prime number.".format(num))