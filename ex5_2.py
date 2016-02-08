def do_n(func, n):
	if n > 0:
		func()
		do_n(func, n-1)

def print_something():
	print "hello world!"

do_n(print_something, 5)