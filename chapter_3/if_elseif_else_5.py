# Statement - If_elif_else
# 0 to 3 - free movie ticket
# 4 to 18 - 150 movie ticket
# 19 to 35 - 250 movie ticket
#36 to above - 200 movie ticket

age = input("Enter your age for ticket purchase: ")
ages = int(age)
if 0<ages<=3:
    print("you can watch movie free")
elif 4<ages<=18:
    print("you can watch movie at 150 rupees")
elif 19<ages<=35:
    print("you can watch movie at 250 rupees")
else:
    print("you can watch movie at 200 rupees")