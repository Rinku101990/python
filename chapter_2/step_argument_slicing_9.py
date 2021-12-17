# step argument slicing
# Syntax - [start argument : stop argument -1 : step]
lang = "Rinku"
print(lang[0:4:1])
print(lang[0::1]) # traverse start to end with step 1 string
print(lang[::1]) # traverse start to end with step 1 string
print(lang[::2]) # traverse with step 2 string
print(lang[-1::-1]) # make string reverse with negative argument
print(lang[::-1]) # reverse output