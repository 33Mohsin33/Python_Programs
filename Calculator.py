ch=int(input("Enter Choice \n1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n"))
if ch!=1 and ch!=2 and ch!=3 and ch!=4:
    print("Wrong Choice ")
else: 
    first=float(input("Enter First number  : "))
    Secnd=float(input("Enter Second number : "))
    if ch==1:
        Add=first+Secnd
        print("Sum = "+str(Add))
    elif ch==2:
        Sub=first-Secnd
        print("Sub = "+str(Sub))
    elif ch==3:
        Mul=first*Secnd
        print("Mul = "+str(Mul))
    else:
        Div=first/Secnd
        print("Div = "+str(Div))

