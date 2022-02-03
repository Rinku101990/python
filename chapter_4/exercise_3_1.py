# Exercise  - 
# Define a function which takes two numbers as a input and return greater of two numbers

def greater(a,b):
    if a > b:
        return a
    else:
        return b

num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))
bigger = greater(num1,num2)
print(f"{bigger} is greater number")