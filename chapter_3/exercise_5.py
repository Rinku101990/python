# for loop example
# sum from 1 to 10

# total = 0
# for i in range(1,11):
#     total += i
# print(total)

# get number by by user to print sum

number = int(input("Enter natural number for sum: "))

total = 0
for i in range(1, number+1):
    total += i
print(total)