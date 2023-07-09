Names=[]
Reg_No=[]
Marks=[]
List=[]
def save():
    global Names
    global Reg_No
    global Marks
    with open("Data_Of_Students.txt","w") as File:
       for i in range(len(Names)):
        name=Names[i]+","
        File.write(name)
        reg=Reg_No[i]+","
        File.write(reg)
        marks=Marks[i]+","
        File.write(marks)
        File.write("\n")
def Load():
    global Names
    Names=[]
    global Reg_No
    Reg_No=[]
    global Marks
    Marks=[]
    List=[]
    with open("Data_Of_Students.txt","r") as File:
     List=File.readlines()
     for line in List:
        line=line.strip().split(",")
        Names.append(line[0])
        Reg_No.append(line[1])
        Marks.append(line[2])
        
if __name__=="__main__":
  Load()
  while(True):
    print("---------Student Registration System----------")
    print("   1.Entry")
    print("   2.Searching")
    print("   3.Deletion")
    print("   4.Modification")
    print("   5.Save")
    print("   6.Display ALL")
    print("   0.Close")
    ch1=input("Choice-->\n")

    match ch1:
     case "1":
           name=input("Enter Name: ")
           Names.append(name)   
           Reg=input("Enter Reg: ")
           Reg_No.append(Reg)   
           marks=input("Enter marks: ")
           Marks.append(marks)   
           print(Names)
           print(Reg_No)
           print(Marks)
           print("Operation Successfull !!")
     case "2":
           r=input("Enter Reg Number: ")
           try:
            r=Reg_No.index(r)
            print(f"Name      : {Names[r] }")      
            print(f"Reg_No    : {Reg_No[r]}")      
            print(f"Marks     : {Marks[r] }")
           except:
            print("No Record Found")      
     case "3":
           r=input("Enter Reg Number: ")
           try:
            r=Reg_No.index(r)
            int(r)
            Names.pop(r)   
            Reg_No.pop(r)
            Marks.pop(r)
            print("Deleted Successfully!!")
           except:
            print("No Record Found")   
     case "4":
            r=input("Enter Reg Number: ")
            r=Reg_No.index(r)
            int(r)
            print(f"Old Name      : {Names[r] }")      
            print(f"Old Reg_No    : {Reg_No[r]}")      
            print(f"Old Marks     : {Marks[r] }")
            name=input("Enter Name: ")
            Names[r]=name
            print(Names[r])
            Reg=input("Enter Name: ")
            Reg_No[r]=Reg
            marks=input("Enter marks: ")
            Marks[r]=marks
            print("Operation Successfull !!")

     case "5":
          save()
     case "6":
            for r in range(len(Names)):
                print(f"Name      : {Names[r]}")
                print(f"Reg_No    : {Reg_No[r]}")
                print(f"Marks     : {Marks[r]}")
                print("    -----     "  )

     case _:
          print("Wrong Entery")
            

        
           


