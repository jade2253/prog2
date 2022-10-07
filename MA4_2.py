#!/usr/bin/env python3.9
from numba import njit
from person import Person
import time as t
import matplotlib as plt
import numpy as np

def fib_py(n):
	if n <= 1:
		return n
	else:
		return fib_py(n-1) + fib_py(n-2)

@njit
def fib_numba(n):
	if n <= 1:
		return n
	else:
		return fib_numba(n-1) + fib_numba(n-2)

def main():
	f = Person(5)
	print(f.get())
	f.set(7)
	toTest = np.arange(30, 46)
	print(toTest)
	resCpp = np.array([])
	print(resCpp)
	#Time for fib in c++
	for i in toTest:
		f.set(i)
		start = t.perf_counter()
		f.fib()
		end = t.perf_counter()
		np.append(resCpp, start-end)
	print(resCpp)
	
	print(fib_py(7))
	print(fib_numba(7))
	print(f.get())

if __name__ == '__main__':
	main()
