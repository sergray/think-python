"""
Write a function called remove_duplicates that takes a list and returns a 
new list with only the unique elements from the original. Hint: they don't have to be in the same order. 
"""

def remove_duplicates(user_list):
	return list(set(user_list))

print remove_duplicates([3, 5, 7, 1, 2, 10, 3, 4, 4, 6, 6, 9])