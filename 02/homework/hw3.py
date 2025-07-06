import ast

l1 = input()
l2 = input()
lf = []

l1 = ast.literal_eval(l1)
l2 = ast.literal_eval(l2)

l3 = l1 + l2

def isnt_in_list(el):
	for idx in lf:
		if (idx == el):
			return 0
	return 1


for el in l3:
	if (isnt_in_list(el)):
		lf.append(el)
lf.sort()		

print(lf)


