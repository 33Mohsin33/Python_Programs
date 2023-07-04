def while_loop():
    s=int(input("From which value loop should start:"))
    e=int(input("At which value loop should Stop:"))
    while s<e:
     print(s,", ",end='')
     s+=1
    else:
      print(s)
def For_Loop():
    s=int(input("From which value loop should start:"))
    e=int(input("At which value loop should Stop:"))
    for i in range(s,e):
     print(i,", ",end='')
print("----- Choice Menu -----")
print("   1. While_Loop")
print("   2. For_Loop")
ch=input("-->")
if ch=="1":
 while_loop()
elif ch=="2":
 For_Loop()
else:
  print("Wrong Entry")