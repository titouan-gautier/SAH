t = [10,2,5,8,6,7,2]

def est_ensemble(t):
	for i in range(len(t)-1) :
		for e in t[i+1:] :
			if t[i] == e :
				return False

	return True 

print(est_ensemble(t)) 
