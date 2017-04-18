"""
yikes... I switched to mathematica...
"""
import itertools

def genNumbs(n):
	l = list(range(n))
	print(l)
	perm = list(itertools.permutations(l))
	return perm

if __name__ == "__main__":
	for i in range(8, 8+1): #need for 50, but at 8 there is still a lot
		print(len(genNumbs(i)))
