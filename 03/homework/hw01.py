dictionary = eval(input())
text_list = eval(input())
result = [dictionary[i] for i in text_list if i in dictionary]
print(" ".join(result))
