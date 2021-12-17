# Question - ask user to input 3 numbers and you have to print average of three numbers using string formating
x,y,z=input("enter 3 numbers").split(",")
# x=int(input("enter first number"))
# y=int(input("enter second number"))
# z=int(input("enter third number"))
total = (int(x)+int(y)+int(z))/3
print(f"Avarage of numbers: {total}")