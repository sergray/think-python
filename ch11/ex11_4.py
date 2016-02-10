"""
def reverse_lookup(d, v):
    for k in d:
        if d[k] == v:
            return k
    raise ValueError

Modify reverse_lookup so that it builds and returns a list of all 
keys that map to v, or an empty list if there are none.
"""

def reverse_lookup(dictionary, value):
	list_of_keys = []

	for key in dictionary:
		if dictionary[key] == value:
			list_of_keys.append(key)
	return list_of_keys

def histogram(word):
	hist_dict = {}

	for char in word:
		hist_dict[char] = 1 + hist_dict.get(char, 0)
	return hist_dict


h = histogram('parrot')
print reverse_lookup(h, 2)
print reverse_lookup(h, 3)
