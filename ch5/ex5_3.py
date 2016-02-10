def check_fermat(a, b, c, n):
	if n > 2 and (a**n + b**n == c**n):
		print "holy smoke, fermat was wrong!"
	else:
		print "no, it doesn't work!"

def user_input():
	x = int(raw_input("Write your first number to check Fermat Theorem: "))
	y = int(raw_input("Write second first number to check Fermat Theorem: "))
	m = int(raw_input("Write your third number to check Fermat Theorem: "))
	n = int(raw_input("Write the power of all numbers: "))
	check_fermat(x, y, m, n)

user_input()