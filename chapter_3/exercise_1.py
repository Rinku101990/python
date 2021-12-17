# EXERCISE - WATCH COCO
# ask user's name and age
# If user name start with ("a" or "A") and age is above 10 then
# Print "You can watch coco movie"
# Else print "Sorry you can not watch coco"

name, age=input("Enter your name and age to watch movie: ").split(",")
name_spdate = name.find("a")
name_cupdate = name.find("A")
age=int(age)
if name_spdate=='a' or name_cupdate=='A' and age==0:
    print("You can watch coco movie")
else:
    print("Sorry, you cannot watch coco movie")