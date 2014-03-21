

import random

def make_matrix(m,n):
	for i in range(0,n):
		a = []
		for j in range(0,n):
			a.append(int(random.random() * 100))
		m.append(a)

def minus_last(m):
	l = len(m)
	for i in range(0,l-1):
		for j in range(0,l):
			m[i][j] = m[i][j] - m[l-1][j]

def print_matrix(m):
	for i in m:
		print(i)
	print()

arr = []

make_matrix(arr,4)
print_matrix(arr)

minus_last(arr)
print_matrix(arr)
