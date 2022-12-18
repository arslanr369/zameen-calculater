print("Welcome to zameen calculater")

while True:
    a = int(input('''
    1 Kanal
    2 Marla 
    3 Foot  Method
    4 karam Method
    5 exit
    '''))
    if a == 1:
     length = eval(input("Enter the lentgh=-"))
     width = eval(input("Enter the width=-"))
     sum = int((length * width) / 272) / 20
     print("Total Kanal=", sum)
    elif a == 2:
     length = eval(input("Enter the lentgh=-"))
     width = eval(input("Enter the width=-"))
     sum = int((length * width) / 272)
     print("Total Marla=", sum)
    elif a == 3:
     length = eval(input("Enter the lentgh=-"))
     width = eval(input("Enter the width=-"))
     sum = int((length * width) / 272)
     print("Total Marla=", sum)
    elif a == 4:
     length = eval(input("Enter the lentgh=-"))
     width = eval(input("Enter the width=-"))
     sum = int((length * width) / 9)
     print("Total Marla=", sum)
    else:
        break

