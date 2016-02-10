"""
Write a function that reads the words in words.txt and stores them as keys in a dictionary. 
It doesn't matter what the values are. Then you can use the in operator as a fast way to 
check whether a string is in the dictionary.
"""
def words_as_dict():
	words_dict = {}
	dict_value = 1

	fin = open('../words.txt')
	for line in fin:
		word = line.strip()
		words_dict[dict_value] = word
		dict_value += 1
	return words_dict

print words_as_dict()
