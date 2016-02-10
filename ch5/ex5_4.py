"""     
	If any of the three lengths is greater than the sum of the other two, 
	then you cannot form a triangle. Otherwise, you can. (If the sum of two lengths equals 
	the third, they form what is called a "degenerate" triangle.) 

    1- Write a function named is_triangle that takes three integers as arguments, 
    and that prints either "Yes" or "No," depending on whether you can or cannot 
    form a triangle from sticks with the given lengths.

    2- Write a function that prompts the user to input three stick lengths, 
    converts them to integers, and uses is_triangle to check whether sticks with the 
    given lengths can form a triangle.
"""

def is_triangle(a, b, c):
	if (a + b < c) or (b + c < a) or (a + c < b):
		print "Not a triangle!"
	elif (a + b == c) or (b + c == a) or (a + c == b):
		print "Degenerate triangle!"
	else:
		print "Yes, triangle!"

def user_input():
	first = int(raw_input("First stick length: "))
	second = int(raw_input("Second stick length: "))
	third = int(raw_input("Third stick length: "))
	is_triangle(first, second, third)

user_input()