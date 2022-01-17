# Break and Continue Loop

#  print 1 to 10
# Break Statement Break loop of statement not execute 
# for i in range(1,11):
#   if i == 5:
#       break
#   print(i)
for i in range(1,5):
    if i == 5:
        break
    print(i)

# Continue Statement
# print 1 to 10 but not 5 
# 1,2,3,4,6,7,8,9,10

for i in range(1,11):
    if i == 5:
        continue
    print(i)