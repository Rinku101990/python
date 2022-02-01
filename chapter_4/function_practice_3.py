# Practice with function
# Question 1-Print last String in charector

def last_char(name):
    return name[-1]
print(last_char("Rinku Vishwakarma"))

# Case 1- If you pass integer then get an error, so if you make function for charector then input only charector not integer 
# print(last_char(9))

# Define Function to check number even or odd ore not
# first way-
def odd_even(num):
    if num%2 == 0:
        return "even"
    else:
        return "odd"

# Second way-
def odd_even(num):
    if num%2 == 0:
        return "even"
    return "odd"

# 3rd way
def odd_even(num):
    if num%2 == 0:
        return True
    return False

# 4rth way
# Pass Argument in Defining Function 
def odd_even(num):
    return num%2 == 0  # true

# pass parameter in funtion call
print(odd_even(10))