# define a function which will take a list containing numbers  as input
# and return a list cantaining square of every elements

# numbers = [1,2,3,4]
# square list - [1,4,9,16]

first = int(input("Enter starting point of numbers = "))
last = int(input("Enter ending point on numbers = "))

numlist = list(range(first,last))

def squarelist(numlist):
    result = []
    for i in numlist:
        result.append(i**2)
    return result

print(squarelist(numlist))