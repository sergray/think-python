"""
Read the documentation of the dictionary method setdefault and use it to write a 
more concise version of invert_dict.

def invert_dict(d):
    inverse = dict()
    for key in d:
        val = d[key]
        if val not in inverse:
            inverse[val] = [key]
        else:
            inverse[val].append(key)
    return inverse
"""

def invert_dict(dictionary):
	inverse = {}

	for key, value in dictionary.iteritems():
		inverse.setdefault(value, []).append(key)
	return inverse

def histogram(word):
	hist_dict = {}

	for char in word:
		hist_dict[char] = 1 + hist_dict.get(char, 0)
	return hist_dict

hist = histogram('ilhanmercan')
print invert_dict(hist)
