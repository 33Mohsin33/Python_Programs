List= [30,20,10,40,50]
print("      01.Finding the index of an element")
print("      02.Modifying elements")
print("      03.Slicing")
print("      04.Appending elements")
print("      05.Removing elements")
print("      06.Length of a list")
print("      07.Sorting a list")
print("      08.Concatenating lists")
print("      09.Copying a list")
print("      10.Checking membership")
print("      11.Counting occurrences")
print("      12.Reversing a list")
print("      13.Clearing a list")
ch=input("--> ")
match ch:
    case "1"  :
     val=int(input("Enter Index: "))
     print("Your Value Is At Index ",List.index(val))
     print("Updated List is : ",List)
    case "2"  :
     val=int(input("Enter Value To Modify: "))
     val2=int(input("Enter New Value: "))
     List[List.index(val)]=val2
     print("Updated List is : ",List)
    case "3"  :
     st=int(input(f"Enter Starting index n<{len(List)-1} "))
     en=int(input(f"Enter Last index n<{len(List)-1} "))
     sliced_list=List[2:4]
     print(sliced_list)
     print(f"List : (From {st} to {en}) index is \n {sliced_list}")
    case "4"  :
     val=int(input("Enter value To Append: "))
     List.append(val)
     print("Updated List is : ",List)
    case "5"  :
     val=int(input("Enter value To Remove: "))
     List.remove(val)
     print("Updated List is : ",List)
    case "6"  :
     print("Length Of a String Is: ",len(List))
    case "7"  :
     List.sort()
     print("Sorted List Is: ",List)
    case "8"  :
     List2=[60,70,30,80,50] #For Concatination
     print(f"{List} + {List2} = {List + List2}")
    case "9"  :
     List3=[]
     print(f"Before Copying : {List3}")
     List3=List.copy()
     print(f"After Copying : {List3}")
    case "10"  :
     val=int(input("Enter value To Check: "))
     if val in List:
      print("Value is Present")
     else:
      print("Not Found")
    case "11" :
      val=int(input("Enter value To Check: "))
      print(f"Value is Present {List.count(val)} time/times")
    case "12" :
     print(f"Before Reversing : {List}")
     List.reverse()
     print(f"After Reversing : {List}")
    case "13" :
     print(f"Before Clearing : {List}")
     List.clear()
     print(f"After Clearing : {List}")

     
      

    

        