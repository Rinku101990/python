# Question - Define is_palindrome function that take one word as input
# and return True if it is palindrome else return False

# Palindrome - Word that read same backwords and forwords

# Example - 
# is_palindrome("madam") ------> True
# is_palindrome("naman") ------> True
# is_palindrome("horse") ------> True

# logic (algorithm)
# step 1 -> reverse the string
# step 2 -> campare reversed string with origin string
# Answer - Palindrome - read string backword and forword be same both side

# Case One
def is_palindrome(a):
    name_reverse = a[::-1]
    if name_reverse == a:
        return True
    else:
        return False

# Case Two
def is_palindrome(a):
    if a[::-1] == a:
        return True
    return False

# Case Three
def is_palindrome(a):
        return a[::-1] == a

name = input("Enter String to check palindrome: ")
print(is_palindrome(name))