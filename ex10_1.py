"""
Write a function called nested_sum that takes a nested list of integers and add up the elements from all of the nested lists.
"""
import math
def nested_sum(nested_list):
	total = 0
	for i in nested_list:
		if isinstance(i, list):
			total = total + nested_sum(i)
		else:
			total = total + i
	print total


#x = [3, 5, [2, 5, [10, 10]], 10, [5, 10]]
x = [3, 5, [2, 5], 10, [5, 10]]

nested_sum(x)