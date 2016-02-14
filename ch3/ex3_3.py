# TODO try to implement that using format and https://docs.python.org/2/library/string.html#format-specification-mini-language
def right_justify(a):
	length = 70 - len(a)

	print length * " " + a