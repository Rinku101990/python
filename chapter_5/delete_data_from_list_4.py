# Delete Data from list
# common method - pop()
# pop() - if you do not pass any parameter in pop method then last item deleted by default other remove by position pop(1)- remove item from 1 position
# remove() - if you want to delete the item but you don't know the position of element in list. so you can use remove() method
# when we use remove method to delete duplicate item from list then first item are delete from list

from distutils.command.build_scripts import first_line_re


fruits = ['graps','orange','mango','apple','kiwi']
# fruits.pop()
# fruits.pop(2)
fruits.remove('kiwi')

print(fruits)
