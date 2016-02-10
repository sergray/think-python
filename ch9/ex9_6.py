"""Write a function called is_abecedarian that returns True 
if the letters in a word appear in alphabetical order (double letters are ok). 
How many abecedarian words are there?
"""
counter = 0

def is_abecedarian():
	#import pdb; pdb.set_trace()
	fin = open('../words.txt')
	for line in fin:
	    word = line.strip()
	    alphabetical(word)

def alphabetical(word_to_check):
	global counter
	for i in range(len(word_to_check)-1):
		if word_to_check[i] > word_to_check[i+1]:
			return False
	counter += 1
	print counter, word_to_check 

is_abecedarian()
