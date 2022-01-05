# Exercise one of three
# sum of natural numbers
# ask a user for natural number(n)
# print total 1 to n

# Case 1 - Sum of natural numbers

i=1
total=0
while i<=10:
    total = total + i
    i=i+1
print(f"Sum of number: {total}")

# Case 2 - Ask user for natural numbers(n)

number = input("Enter any natural no for sum: ")
numbs = int(number)
i=1
total=0
while i<=numbs:
    total = total + i
    i=i+1
print(f"Sum of number: {total}")

# Case 3 - Print natural no

number = input("Enter any natural no for sum: ")
numbs = int(number)
i=1
while i<=numbs:
    print(f"{i}")
    i=i+1