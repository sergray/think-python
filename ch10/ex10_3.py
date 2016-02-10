"""
Write a function that takes a list of numbers and returns the cumulative sum; 
that is, a new list where the ith element is the sum of the first i+1 elements 
from the original list. For example, the cumulative sum of [1, 2, 3] is [1, 3, 6]. 
"""

def cumulative_sum(user_list):
	cum_list = []
	total = 0

	for i in user_list:
		total += i
		cum_list.append(total)
	return cum_list

x = [1, 2, 3, 4]
print cumulative_sum(x)

