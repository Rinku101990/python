# String Formatting
name="Rinku Vishwakarma"
age=30
print("Hi "+name+ "Your age is "+ str(age)) # ugly syntex

# Python 3 Syntax - {}-Placeholder
print("Hi {} your age is {}".format(name,age))
# Python 3.6 Syntax
print(f"Hi {name} your age is {age}")
# Also in string formationg yuo can calculate(addtion,Substraction,multiplication,division) values
print("Hi {} your age is {}".format(name,age+2))
print(f"Hi {name} your age is {age+2}")