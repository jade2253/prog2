#!/usr/bin/env python3.9
from numba import njit
from person import Person
import time as t

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
		return fib_py(n-1) + fib_py(n-2)

def main():
	f = Person(5)
	print(f.get())
	f.set(7)
	res = f.fib()
	print(res)
	print(f.get())

if __name__ == '__main__':
	main()
