# Strip Method - remove space from string
name = "  Rinku  "
dots = "............"
# remove left side space using - lstrip() method
print(name + dots)
# remove left side spade using lstrip() method
print(name.lstrip() + dots)
# remove right side spade using rstrip() method 
print(name.rstrip() + dots)
# remove left and right space using one method - strip() method
print(name.strip() + dots)
# remove all sapces between string and left,right or other - by replace([first argument,second argument]) method 
name1 = " Rin  ku "
print(name.replace(" ",""))