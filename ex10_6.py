"""
Write a function called is_sorted that takes a list as a parameter and returns True 
if the list is sorted in ascending order and False otherwise. You can assume (as a precondition) 
that the elements of the list can be compared with the relational operators <, >, etc.

For example, is_sorted([1,2,2]) should return True and is_sorted(['b','a']) should return False. 
"""

def is_sorted(user_list):
	not_sorted_list = user_list[0:len(user_list)]
	user_list.sort()
	sorted_list = user_list
	if not_sorted_list == sorted_list:
		return True
	else:
		return False



x = [3, 5, 7, 1, 1, 2]
y = [1, 1, 2, 2, 3, 4]
print is_sorted(x)
print is_sorted(y)