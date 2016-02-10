"""
Give me a word with three consecutive double letters. I'll give you a couple of words 
that almost qualify, but don't. For example, the word committee, c-o-m-m-i-t-t-e-e. 
It would be great except for the 'i' that sneaks in there. Or Mississippi: M-i-s-s-i-s-s-i-p-p-i. 
If you could take out those i's it would work. But there is a word that has three consecutive 
pairs of letters and to the best of my knowledge this may be the only word. Of course there are 
probably 500 more but I can only think of one. What is the word? 
"""

count_all = 0
def is_triple_double(word_to_check):
	global count_all
	i = 0
	#import pdb; pdb.set_trace()
	count_doubles = 0
	while i < len(word_to_check)-1:
		if word_to_check[i] == word_to_check[i+1]:
			count_doubles += 1
			if count_doubles == 3:
				print "YES This is triple!", word_to_check
				count_all += 1
			i += 2
		else:
			count_doubles = 0
			i += 1
	return False

def find_triple_double():
	global count_all
	fin = open('../words.txt')
	for line in fin:
	    word = line.strip()
	    is_triple_double(word)

	print "TOTAL =", count_all


find_triple_double()