"""
Write a function that reads the file words.txt and builds a list with one element per word. 
Write two versions of this function, one using the append method and the other using the 
idiom t = t + [x]. Which one takes longer to run? Why?
"""
import time

def list_of_words_with_append():
	words_list = []
	fin = open('../words.txt')
	for line in fin:
	    word = line.strip()
	    words_list.append(word)
	return words_list

def list_of_words_with_addition():
	words_list = []
	fin = open('../words.txt')
	for line in fin:
		word = line.strip()
		#import pdb; pdb.set_trace()
		words_list += [word]
	return words_list


""" This part is added from book """
start_time = time.time()
t = list_of_words_with_append()
elapsed_time = time.time() - start_time

print len(t)
print t[:10]
print elapsed_time, 'seconds'

start_time = time.time()
t = list_of_words_with_addition()
elapsed_time = time.time() - start_time

print len(t)
print t[:10]
print elapsed_time, 'seconds'