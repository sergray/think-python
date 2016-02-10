def first(user_input):
	return user_input[0]

def last(user_input):
	return user_input[-1]

def middle(user_input):
	return user_input[1:-1]

def is_palindrome(user_input):
	if len(user_input) <= 1:
		return True
	elif first(user_input) != last(user_input):
		return False
	return is_palindrome(middle(user_input))

print is_palindrome('ahmet')
print is_palindrome('anbbna')