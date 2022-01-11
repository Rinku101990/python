# ask user a number like 12456
# calculate sum of digit 1+2+4+5+6

number = input("Enter number for sum: ")
# print(len(number))
numbers = int(number)
total = 0
for i in range(len(number)):
    total +=int(number[i])
print(total)
