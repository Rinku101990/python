# Function Inside Function

def greater(a,b):
    if a > b:
        return a
    else:
        return b

def greatest(a,b,c):
    bigger = greater(a,b)
    return greater(bigger,c)

num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))
num3 = int(input("Enter Third Number: "))

print(greatest(num1,num2,num3))