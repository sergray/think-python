"""
Memoize the Ackermann function from Exercise ex6_5.py and see if memoization 
makes it possible to evaluate the function with bigger arguments.
"""

def ackermann(m, n):
	ack = {}
	if not isinstance(m, int) or not isinstance(n, int):
		return "Inputs are not integer"
	elif m == 0:
		return n+1
	elif m>n and n==0:
		return ackermann(m-1, 1)
	try:
		return ack[m, n]
	except (KeyError):
		ack[m, n] = ackermann(m-1, ackermann(m, n-1))
		return ack[m, n]

print ackermann("ahmet", 3)
print ackermann(3, "21121")
print ackermann(3, 4)
print ackermann(0, 6)
print ackermann(3, 0)
