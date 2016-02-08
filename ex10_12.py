"""
Two words are a "reverse pair" if each is the reverse of the other. Write a program 
that finds all the reverse pairs in the word list. 
"""

def is_reverse_pair(word):
	if word[0:len(word)-1] == word[len(word)-1:0:-1]:
		return True
	else:
		return False

def read_from_words():
	reverse_pair_words = []
	fin = open('words.txt')
	for line in fin:
		word = line.strip()
		if is_reverse_pair(word) == True:
			reverse_pair_words.append(word)

	print reverse_pair_words

read_from_words()