List=[]
Tuple=(30,20,10,10,50)
print("      01.Search By index")
print("      02.Slicing")
print("      03.Count")

ch=input("--> ")
match ch:
    case "1"  :
     val=int(input("Enter Index: "))
     print("Your Value Is At Index ",Tuple.index(val))
    case "2"  :
     st=int(input(f"Enter Starting index n<{len(Tuple)-1} "))
     en=int(input(f"Enter Last index n<{len(Tuple)-1} "))
     sliced_Tuple=Tuple[2:4]
     print(sliced_Tuple)
     print(f"Tuple : (From {st} to {en}) index is \n {sliced_Tuple}")
    case "3"  :
     val=int(input("which value u want to Count: "))
     print(f"{val} is {Tuple.count(val)} times")
     

     
    