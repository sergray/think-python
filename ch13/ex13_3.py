"""
Modify the program from the previous exercise (ex13_2.py) to print the 20 most frequently-used words in the book.
"""

from string import punctuation, whitespace
from collections import Counter

def most_used_words(file_name):
	counter = dict()
	checked_word = ''
	with open('../'+file_name, 'r') as file:
		# go line by line, seperate words in every line, then check for every character
		for line in file:
			for word in line.split():
					for char in word:
						if char in punctuation or char in whitespace or char.isdigit():
							break
						else:
							# a checked word without punctuation or whitespace or digits
							checked_word += char.lower()
					if checked_word != '':
	  					counter[checked_word] = counter.get(checked_word, 0) + 1
	  				# reset checked_word for next word to check
	  				checked_word = ''

	# to find 20 most frequently used words: http://stackoverflow.com/a/22916447
	most_used_twenty_words = dict(Counter(counter).most_common(20))
  	for key, value in most_used_twenty_words.items():
  		print key, "(" + str(value) + ")",

most_used_words("book.txt")