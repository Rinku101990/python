# Fibonacci Series - 0, 1 - sum of previous two number 
# 0,1,1,2,3,5,8 - When you want to print number in single line. so use end=" "

def fibonacci(num):
    a, b = 0, 1
    while a < num:
        print(a, end=" ")
        a, b = b, a+b
num1 = int(input("Enter Number for Fibonacci Series: "))
fibonacci(num1)