# Variable Scope
# Whose Variable are defined within function in called local variable, 
# If variable are out side of the function is called global

x = 5 # This is global Variable

def func():
    global x # If assign gloable variable with in function,but this is not write way to change global variable value.
    x = 7 # local Variable
    return x

print(x)
print(func())