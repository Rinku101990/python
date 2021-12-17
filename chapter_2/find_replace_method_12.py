# find() and replace() method
word = "she is beautiful and she is good dancer"
# syntax - [which word,replace by word, how many]
print(word.replace("is","was",1))
# find() - [which word, from which position]
is_pos1=word.find("is",1)
print(is_pos1)
print(word.find("is",is_pos1+1))

