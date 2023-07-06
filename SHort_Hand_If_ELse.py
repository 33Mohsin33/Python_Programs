marks=int(input("Enter Marks    %\b\b\b\b"))
# Nomal IF ELse
if marks>=80 and marks<=100: 
 print("A") 
if marks>=80 and marks<=100: 
 print("A") 
elif marks>=70 and marks<=80:
 print("B") 
elif marks>=60 and marks<=70:
  print("C")
else:
  print("Fail")

# Shorthand If Else
print("A") if marks>=80 and marks<=100 else print("B") if marks>=70 and marks<=80 else print("C") if marks>=60 and marks<=70 else print("Fail")