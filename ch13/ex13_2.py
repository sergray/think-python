"""
Go to Project Gutenberg (http://gutenberg.org) and download your favorite 
out-of-copyright book in plain text format.

Modify your program from the previous exercise to read the book you downloaded, 
skip over the header information at the beginning of the file, and process 
the rest of the words as before.

Then modify the program to count the total number of words in the book, 
and the number of times each word is used.

Print the number of different words used in the book. Compare different books 
by different authors, written in different eras. Which author uses the most extensive vocabulary? 
"""

from string import punctuation, whitespace

def counter_words_in_file(file_name):
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

  	print "Total used words:", len(counter)
  	# you can print whole words used in the file with below line.
  	# print counter 

counter_words_in_file("book.txt")
