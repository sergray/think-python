"""
Write a function named uses_all that takes a word and a string of required letters, 
and that returns True if the word uses all the required letters at least once."""


def uses_all(word, required_letters):

	for letter in required_letters:
		if not letter in word:
			return False
	
	return True

print uses_all("ahmet", "hasan")
print uses_all("ahmet", "ahmah")