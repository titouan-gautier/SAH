squares = [1, 2, 3, 3, 5, 3, 8, 3]

def compte(el,list) :
	res = 0
	for i in range(len(squares)) :
		if squares[i] == el :
			res = res + 1
	return res
print(compte(3,squares))
	

