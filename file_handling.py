import os

ch = int(input("Enter a choice\n1.Create a file\n2.Delete the file\n3.Write in the file\nChoice : "))
if ch==1:
    if os.path.exists("New file.txt"):
        print("File already exists")
    
    else:
        f = open("New file.txt","w")
        f.close()
        print("File has been created")
elif ch == 2:
    if os.path.exists("New file.txt"):
        os.remove("New file.txt")
        print("File deleted")
    else:
        print("File not found")
elif ch == 3:
    msg = input("Enter message : ")
    if os.path.exists("New file.txt"):
        f = open("New file.txt","a")
        f.write("\n")
        f.close()
        
        f = open("New file.txt","a")
        f.write(msg)
        f.close()
        print("File written")
    else:
        print("File not found")
    
else:
    print("Invalid input\nOperation terminated")