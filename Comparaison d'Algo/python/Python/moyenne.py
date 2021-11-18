t = {10,2,5,8,4,6,9}

def moyenne(t):
	i = 0
	s = 0 
	y = 0
	for e in t :
		i = i +1
		s = e + s
	y = s / i
	return y
print(moyenne(t))
