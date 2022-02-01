# How to use for loop in string

# Old way - This code valid for JS,Python and so on
name="Rinku Vishwakarma"
for i in range(len(name)):
    print(name[i])

# In Python String are iterable - Python Style
name = "Rinku"
for i in name:
    print(i)

# Make sum of number - input by user and make sum
num = input("Enter number for sum: ")
total = 0
for i in num:
    total += int(i)
print(total)