val=input("Enter Any value Between 5 and 10 : ")
if val.isnumeric()==True:
 val=int(val)
 if val<5 or val >10:
  raise ValueError("Value Must Be between 5 and 10")
else:
 raise ValueError("Value Must Be Intiger")
print("Program Executed Succeddfully")