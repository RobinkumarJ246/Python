f = open("textfile.txt","r")
for x in f:
    print(x)
    
f = open("textfile.txt","w")
f.write("Hi i am here (edited)")
f.close()

f = open("textfile.txt","r")
for x in f:
    print(x)
    
f = open("textfile.txt","a")
f.write("\nI am playing chess")
f.close()

f = open("textfile.txt","r")
for x in f:
    print(x)