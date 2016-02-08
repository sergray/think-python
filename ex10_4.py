"""
Write a function called middle that takes a list and returns a new list that contains all 
but the first and last elements. So middle([1,2,3,4]) should return [2,3].
"""
def middle(user_list):
	last = len(user_list) - 1
	user_list.pop(last)
	user_list.pop(0)
	return user_list


a_list = [1, 3, 10, 2, 5, 4, 6, 8]
print middle(a_list)