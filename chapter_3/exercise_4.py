# ask a user for name
# Example:- Rinku Vishwakarma
# print count of each words
# output: 
    # R - 2
    # i - 2
    # n - 1
    # k - 2
    # u - 1
    # V - 1
    # s - 1
    # h - 1
    # w - 1
    # a - 3
    # m - 1

name = input("Enter your name: ")
temp_val = ""
i = 0
while i < len(name):
    # check duplicate charector in name
    if name[i] not in temp_val: 
        temp_val += name[i]
        print(f"{name[i]} : {name.count(name[i])}")
    i+=1