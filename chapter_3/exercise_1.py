# EXERCISE - WATCH COCO
# ask user's name and age
# If user name start with ("a" or "A") and age is above 10 then
# Print "You can watch coco movie"
# Else print "Sorry you can not watch coco"

name, age=input("Enter your name and age to watch movie: ").split(",")
name_update = name.lower()
age=int(age)
if name_update.find('a') and age==10:
    print("You can watch coco movie")
else:
    print("Sorry, you cannot watch coco movie")