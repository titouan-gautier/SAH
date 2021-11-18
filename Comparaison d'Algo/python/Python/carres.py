squares = [1, 2, 3, 3, 5, 3, 8, 3]
squares2=[]
def carres(list) :

	for i in range(len(squares)) :

		squares2.append ([squares[i]**2 ])
	return squares2
print(carres(squares2))
	

