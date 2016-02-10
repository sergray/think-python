prefixes = 'JKLMNOPQ'
suffix = 'ack'

for letter in prefixes:
	if letter is "O" or "Q":
		print letter + "u" + suffix
	else:
		print letter + suffix