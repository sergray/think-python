"""
Write a function named uses_only that takes a word and a string of letters, 
and that returns True if the word contains only letters in the list
"""


def uses_only(word, usable_letters):

	for letter in usable_letters:
		if not letter in word:
			return False

	return True

print uses_only("ahmet", "hma")
print uses_only("ahmet", "alm")
