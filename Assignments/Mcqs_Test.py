import os
import time

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
Q=["What is the value of π (pi) approximately?",
   "What is the square root of 64?",
   "Value of x in 2x + 5 = 15?",
   "What is the perimeter of a rectangle with length 6 cm and width 4 cm?",
   "Solve for y: 3y + 8 = 20",
   "Which of the following is a composite number?",
   "Calculate the area of a circle with radius 5 cm.",
   "Find the missing number in the pattern: 3, 6, 9, __, 15.",
   "Simplify the expression: (4 + 2)^.",
   "What is the value of 3^2 + 4^2?",
   "What is the value of X if Y=10,X+Y=20"]
Score=0
int(Score)
Correct=("A"      , "C", "D" ,   "C"  , "B",        "A", "D" , "C" , "B" , "A")
A      =("3.14159", "9", "09", "25 cm", "5","78.54 cm²", "2" , "10", "20", "10")
B      =("3.9"    , "7", "10", "15 cm", "4","7.4 cm²"  , "11", "11", "64", "20")
C      =("2.14"   , "8", "60", "20 cm", "0","8.54 cm²" , "9" , "12", "10", "30")
D      =("4.1"    , "6", "05", "10 cm", "8","54 cm²"   , "12", "3" , "35", "40")
for i in range(10):
 time.sleep(1)
 clear_screen()
 print(f"   Q{i+1}:",Q[i])
 print("    A :",A[i])
 print("    B :",B[i])
 print("    C :",C[i])
 print("    D :",D[i])
 ch=input("-->")
 if ch.upper()==Correct[i]:
  Score=Score+10
  print("        Correct Answer '+10' ")
 else:
  Score=Score-5
  print("        Wrong Answer '-10' ")
print("-------> Total Score = ",Score," <---------")