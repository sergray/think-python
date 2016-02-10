"""
Dictionaries have a method called get that takes a key and a default value. 
If the key appears in the dictionary, get returns the corresponding value; 
otherwise it returns the default value. For example:
>>> h = histogram('a')
>>> print h
{'a': 1}
>>> h.get('a', 0)
1
>>> h.get('b', 0)
0


Use get to write histogram more concisely. You should be able to eliminate the if statement. 

def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d
"""

def histogram(word):
	hist_dict = {}

	for char in word:
		hist_dict[char] = 1 + hist_dict.get(char, 0)

	return hist_dict

print histogram("ilhanmercan")