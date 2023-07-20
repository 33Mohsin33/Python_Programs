import random
Encode={
          'a': '!',
          'b': '@',
          'c': '#',
          'd': '$',
          'e': '%',
          'f': '^',
          'g': '&',
          'h': ':',
          'i': ')',
          'j': '(',
          'k': '/',
          'l': '-',
          'm': '=',
          'n': '+',
          'o': '*',
          'p': '|',
          'q': '[',
          'r': ']',
          's': '{',
          't': '}',
          'u': '_', 
          'v': '`',
          'w': '~',
          'x': ' ',
          'y': '3',
          'z': '5',
          'A': '+!',
          'B': '+@',
          'C': '+#',
          'D': '+$',
          'E': '+%',
          'F': '+^',
          'G': '+&',
          'H': '+:',
          'I': '+)',
          'J': '+(',
          'K': '+/',
          'L': '+-',
          'M': '+=',
          'N': '++',
          'O': '+*',
          'P': '+|',
          'Q': '+[',
          'R': '+]',
          'S': '+{',
          'T': '+}',
          'U': '+_', 
          'V': '+`',
          'W': '+~',
          'X': '+ ',
          'Y': '-3',
          'Z': '-5',
          ' ': 'SCP'
          }
Decode= {value: key for key, value in Encode.items()}

asciii=[]
j=0
inp=input("Enter Any Paragraph To Encrypt it (Only_Alphabets)\n")
for i in range(0,len(inp)):
    ch=Encode[inp[i]]
    asciii.append(ch)
    random_key = random.choice(list(Encode.values()))
    asciii.append(random_key)
    random_key = random.choice(list(Encode.values()))
    asciii.append(random_key)
    random_key = random.choice(list(Encode.values()))
    asciii.append(random_key)
print("\nEncoded : ",end="") 
for i in range(len(asciii)):
    print(asciii[i],end="")
print("\nDecoded: ",end="")
for i in range(0,len(asciii),4) :
    print(Decode[asciii[i]],end="")
     