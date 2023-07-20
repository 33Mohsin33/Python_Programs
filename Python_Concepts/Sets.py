set1=set()
set2=set()
print("Enter 3 Values in Each For 2 Sets")
for j in range(2):
 for i in range(3):
  val=input(f"Enter Value {i+1} for set {j+1}: ")
  if j==0:
   set1.add(val)
  else:
   set2.add(val)
print("Intersection         : ",set1.intersection(set2))  
print("union                : ",set1.union(set2))  
print("symmetric_difference : ",set1.symmetric_difference(set2))  
print("Isdisjoint           : ",set1.isdisjoint(set2))  
print(".issubset            : ",set1.issubset(set2))  
print(".issuperset          : ",set1.issuperset(set2))  
