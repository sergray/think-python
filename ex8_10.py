#import pdb; pdb.set_trace()

def palindrome(word):
	length = len(word) - 1
	if word[0:length] == word[length:0:-1]:
		return True
	else:
		return False

print palindrome("anna")
print palindrome("ilhan")