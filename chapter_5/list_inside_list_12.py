# List inside list

matrix = [[1,2,3,4],[5,7,8],[11,21,22]]  # list inside list - 2d list

print(matrix[0])

# using loop
for sublist in matrix:
    for i in sublist:
        print(i)


# for single element
matrix[2][0]

# Find the type

print(type(matrix))