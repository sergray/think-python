"""
Two words are anagrams if you can rearrange the letters from one to spell 
the other. Write a function called is_anagram that takes two strings and 
returns True if they are anagrams. 
"""

def is_anagram(word1, word2):
	for letter in word1:
		if not letter in word2:
			return False
	return True

print is_anagram("mami", "imam")
print is_anagram("haydar", "ilhan")
print is_anagram("bahri", "ihbar")