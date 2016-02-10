def has_no_e():
	fin = open('../words.txt')
	counter = 0 # count total words
	count_e = 0 # count words without 'e' letter

	for line in fin:
	    word = line.strip()
	    counter += 1
	    if not 'e' in word:
	    	print word
	    	count_e += 1

	percentage = float(count_e) / counter
	print percentage
	
has_no_e()