# input two number and make addition(int function - change string to integer)
number1=input("enter first number\n") # get input as string
number2=input("enter second nuber\n") # get input as string
total = number1 + number2
print("Sum of number: "+total)

number3 = int(input("enter first number\n"))
number4 = int(input("enter second number\n"))
total_of_number = number3 + number4
# you can't add string with integer but use str function(change int to string) to add string with integer
print("Sum of number: "+str(total_of_number))

number5=str(4)
number6=float("4")
number7=int("4")
print(number6 + number7) # get output always in float