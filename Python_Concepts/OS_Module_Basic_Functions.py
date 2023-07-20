print("----------OS Module FUNCtions-------")
import os
print("1.Create Folder")
print("2.Delete Folder")
print("3.Rename Folder")
ch=input("Enter Choice: \n    ")
match ch:
 case "1":
    ch=int(input("How much u want to create folders : "))
    while True:
        if ch==0:
         break
        name=input("Enter Folder Name U want to Create : ")
        try:
            os.mkdir(name)
            ch-=1
        except:
            print("Already Exist")
 case "2":
    name=input("Enter Folder Name U want to Delete : ")
    os.remove(name)    
 case "3":
    o_name=input("Enter Older Name:")
    Name=input("Enter New Name:")
    os.rename(o_name,Name)

