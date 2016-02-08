"""
The (so-called) Birthday Paradox:

    Write a function called has_duplicates that takes a list and returns True if there is any 
    element that appears more than once. It should not modify the original list.

    If there are 23 students in your class, what are the chances that two of you have 
    the same birthday? You can estimate this probability by generating random samples of 23 
    birthdays and checking for matches. Hint: you can generate random birthdays with the 
    randint function in the random module. 

You can read about this problem at http://en.wikipedia.org/wiki/Birthday_paradox, 
and you can download my solution from http://thinkpython.com/code/birthday.py.
"""
import random

def has_duplicates(birthday_list):
	"""Return true if there are duplicate birthdays"""

	if len(birthday_list) == len(set(birthday_list)):
		return False
	else:
		return True

def random_birthday(n):
    """Returns a list of integers between 1 and 365, with length (n)."""
    birthdays = []
    for i in range(n):
        bday = random.randint(1, 365)
        birthdays.append(bday)
    #import pdb; pdb.set_trace()
    return birthdays


print has_duplicates(random_birthday(40))