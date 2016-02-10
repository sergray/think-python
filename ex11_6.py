"""
Run this version of fibonacci and the original with a range of parameters and compare their run times.
"""
import time


def fibonacci1(n):
	known = {0:0, 1:1}

	if n in known:
		return known[n]

	res = fibonacci1(n-1) + fibonacci1(n-2)
	known[n] = res
	return res

def fibonacci2(n):
    if n == 0:
        return 0
    elif  n == 1:
        return 1
    else:
        return fibonacci2(n-1) + fibonacci2(n-2)


start_time = time.time()
t = fibonacci1(20)
elapsed_time = time.time() - start_time
print elapsed_time, 'seconds'

start_time = time.time()
t = fibonacci2(20)
elapsed_time = time.time() - start_time
print elapsed_time, 'seconds'