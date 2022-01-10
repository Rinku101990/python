# ask user to number  containing more than one digit
# example = 12345
# calculate 1+2+3+4+5 and print

# algorithem(method to solve problem in human langauge)
# do not change input in int
# pick string charector one by one and change to int
# int(example[0]+example[1]....+example[n])

number = input("Enter number more than one digit: ")
total = 0
i = 0
while i < len(number):
    total += int(number[i])
    i += 1
print(total)
