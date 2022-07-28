# More Method to add items in a list

# Using apend method to add item in last

# using insert method to add item at any position

# using cancatenate add to two sting

# using extent method

# difference b/w apend and extent - apend add item with list=['graps', 'apple', 'mango', ['mango']]
#  and extent add item in list =['graps', 'apple', 'mango']

fruits = ['graps','apple']

fruits1 = ['graps','apple']

fruits2 = ['mango']

fruits.insert(1, "orange")

fruits = fruits1 + fruits2

fruits1.extend(fruits2)
# fruits1.append(fruits2)

print(fruits1)



