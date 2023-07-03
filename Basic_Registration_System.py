print("------------------Student List---------------")
S_List=[]
while True:
 S_List.sort
 print("1.Display\n2.Add\n")
 ch=int(input("-->"))
 if ch==1 :
    print("1.Reg_No\n2.Names\n3.Marks\n")
    ch=int(input("-->"))
    if ch==1 :
       for i in S_List[::2]:
        print(i)
    elif ch==2 :
       for i in S_List[1::2]:
        print(i)
    elif ch==3 :
       for i in S_List[2::2]:
        print(i)
 elif ch==2 :
  
       reg=int(input("Enter Reg_No: "))
       S_List.append(reg)
       reg=input("Enter Name: ")
       S_List.append(reg)
       reg=input("Enter marks: ")
       S_List.append(reg)
   