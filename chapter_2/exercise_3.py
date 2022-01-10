# take two comma seperated input from user
# 1-user name
# 2-a single charector

# Output - 2 print lines
# user name length
# count the charector that user inputed(bonus-case sensitive)

name,text = input("enter name and search single text: ").split(",")
print(len(name))
print(name.count(text)) # find charector with case sentive
# Make name,search text lower then find charector(case sensitive and insensitive
# if user put search text with space then how to manage search charector - strip method to next step
