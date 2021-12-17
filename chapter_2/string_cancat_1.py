# String Cancatenation() - can't add string with number - only string to string and integer to integer
first_name="Rinku"
last_name="Vishwakarma"
my_name = first_name +" "+ last_name
# print(my_name)
mobile_number = "9065432189"
my_info = my_name+" "+mobile_number
print(my_info)
print(my_info+str(10)) # no error
print(my_info+10) # error
print(my_info+"3") # no error
# you can't apply addtion of string with integer but multiplication you can
print(my_info*3)