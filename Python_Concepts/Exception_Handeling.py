def Div():
 try:
  dividend = int(input("Enter the dividend: "))
  divisor = int(input("Enter the divisor(Enter Zero): "))
  quotient = dividend / divisor
  print("Quotient:", quotient)
        return 1
 except ValueError:
        print("Invalid input! Please enter integers.")
        return 0
 except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
        return 0

 finally:
        print("Byee")
Div()
