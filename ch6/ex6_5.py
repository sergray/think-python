"""
See http://en.wikipedia.org/wiki/Ackermann_function. Write a function named ack 
that evaluates Ackermann's function. Use your function to evaluate ack(3, 4), 
which should be 125. What happens for larger values of m and n?
"""

def ackermann(m, n):
	if not isinstance(m, int) or not isinstance(n, int):
		return "Inputs are not integer"
	elif m == 0:
		return n + 1
	elif m > 0 and n == 0:
		return ackermann(m-1, 1)
	elif m > 0 and n > 0:
		return ackermann(m-1, ackermann(m, n-1))

print ackermann("ahmet", 3)
print ackermann(3, "21121")
print ackermann(3, 4)
print ackermann(0, 6)
print ackermann(3, 0)
#print ackermann(10000, 1212121) # RuntimeError: maximum recursion depth exceeded

