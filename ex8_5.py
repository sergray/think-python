def count(str, letter):
	word = str
	count = 0
	for letter in word:
	    if letter == 'a':
	        count = count + 1
	print count

count ("ilhan mercan", "a")