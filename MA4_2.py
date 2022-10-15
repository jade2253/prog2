#!/usr/bin/env python3
from numba import njit
from person import Person
import time as t
import matplotlib.pyplot as plt
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
		resCpp = np.append(resCpp, end - start)
	print(resCpp)
	#Time for fib with Numba
	resNumba = np.array([])
	for i in toTest:
		start = t.perf_counter()
		fib_numba(i)
		end = t.perf_counter()
		resNumba = np.append(resNumba, end - start)
	print(resNumba)
	#Time for fib with python
	# resPy = np.array([])
	# for i in (toTest-6):
	# 	start = t.perf_counter()
	# 	fib_py(i)
	# 	end = t.perf_counter()
	# 	resPy = np.append(resPy, end - start)
	# print(resPy)

	plt.plot(resNumba, 20)
	# plt.plot(resCpp, 20)
	# ax.plot(resPy, 20)
	plt.legend(['Numba', 'Cpp'])
	plt.savefig('Time to compute Fib')
	print(fib_py(7))
	print(fib_numba(7))
	print(f.get())

if __name__ == '__main__':
	main()
