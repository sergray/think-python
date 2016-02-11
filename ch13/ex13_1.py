"""
Write a program that reads a file, breaks each line into words, strips whitespace 
and punctuation from the words, and converts them to lowercase.

Hint: The string module provides strings named whitespace, which contains space, tab, newline, 
etc., and punctuation which contains the punctuation characters. Let's see if we can make Python swear:

>>> import string
>>> print string.punctuation
!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~

Also, you might consider using the string methods strip, replace and translate. 
"""
from string import punctuation, whitespace

def exercise13_1():
	checked_word = ''
	fin = open('../words.txt')

	for line in fin:
		word = line.strip()
		for char in word:
			if char in punctuation or char in whitespace:
				pass
			else:
				checked_word += char.lower()
		print word

exercise13_1()
