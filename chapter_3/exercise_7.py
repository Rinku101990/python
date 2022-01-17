# practise for loop
# ask name for user and count each charector

name = input("Enter your name: ")
temp_value = ''
# i = 0
for i in range(len(name)):
    if name[i] not in temp_value:
        temp_value += name[i]
        print(f"{name[i]} : {name.count(name[i])}")