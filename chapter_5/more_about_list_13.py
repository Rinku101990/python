# More about list
# range function
# pap function
# index function
# pass list to a function

# range function in list


numbers = list(range(1,11))   # list method with range function
print(numbers)
# pop mehtod
poppeditem = numbers.pop()
print(poppeditem)


# Index method - return first occurenece of element otherwise mention position

indposition = numbers.index(1)
print(indposition)
# indpositionby = numbers.index(1, 8, 10)  # mention starting point to find element position terminate end position
# print(indpositionby)

# Pass function in list
l = [1,2,3,4,5,6,7,8,9]
def negativelist(l):
    negative = []
    for i in l:
        negative.append(-i)
    return negative

print(negativelist(l))

