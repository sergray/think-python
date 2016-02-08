"""
Write a function called chop that takes a list, modifies it by removing the first and last elements, and returns None.
"""

def chop(user_list):
	last = len(user_list) - 1
	del user_list[last]
	del user_list[0]
	return None