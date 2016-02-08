"""
I was driving on the highway the other day and I happened to notice my odometer. Like most odometers, 
it shows six digits, in whole miles only. So, if my car had 300,000 miles, for example, I'd see 3-0-0-0-0-0.

"Now, what I saw that day was very interesting. I noticed that the last 4 digits were palindromic; 
that is, they read the same forward as backward. For example, 5-4-4-5 is a palindrome, 
so my odometer could have read 3-1-5-4-4-5.

"One mile later, the last 5 numbers were palindromic. For example, it could have read 3-6-5-4-5-6. 
One mile after that, the middle 4 out of 6 numbers were palindromic. And you ready for this? 
One mile later, all 6 were palindromic!

"the question is, what was on the odometer when I first looked?"
"""


# Not an efficient solution at all, but it was the first solution that it came to my mind.
# Later, when I looked back to book for solution, I saw the one below my solution.


def is_palindromic():
	#import pdb; pdb.set_trace()
	last = str(999999)
	start = str(100000)

	while start < last:
		if start[2:6] == start[6:1:-1]:
			start = int(start) + 1
			start = str(start)
			if start[1:6] == start[6:0:-1]:
				start = int(start) + 1
				start = str(start)
				if start[1:5] == start[4:0:-1]:
					start = int(start) + 1
					start = str(start)
					if start[0:6] == start[6::-1]:
						print "Yes, that's it:", int(start) - 3
					else:
						start = int(start) + 1
						start = str(start)
				else:
					start = int(start) + 1
					start = str(start)
			else:
				start = int(start) + 1
				start = str(start)
		else:
			start = int(start) + 1
			start = str(start)


is_palindromic()


# def has_palindrome(i, start, len):
#     """Returns True if the integer i, when written as a string,
#     contains a palindrome with length (len), starting at index (start).
#     """
#     s = str(i)[start:start+len]
#     return s[::-1] == s
    

# def check(i):
#     """Checks whether the integer (i) has the properties described
#     in the puzzler.
#     """
#     return (has_palindrome(i, 2, 4)   and
#             has_palindrome(i+1, 1, 5) and
#             has_palindrome(i+2, 1, 4) and
#             has_palindrome(i+3, 0, 6))


# def check_all():
#     """Enumerates the six-digit numbers and prints any that satisfy the
#     requirements of the puzzler"""

#     i = 100000
#     while i <= 999996:
#         if check(i):
#             print i
#         i = i + 1


# print 'The following are the possible odometer readings:'
# check_all()
# print

