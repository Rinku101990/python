# Find Greatest no from 3 argument in function

def greatest(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c

num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))
num3 = int(input("Enter Third Number: "))

print(greatest(num1,num2,num3))