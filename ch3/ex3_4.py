"""
do_twice(print_spam)

1/ Type this example into a script and test it.
2/ Modify do_twice so that it takes two arguments, a function object and a value, and calls the 
function twice, passing the value as an argument.
3 Write a more general version of print_spam, called print_twice, that takes a string as a 
parameter and prints it twice.
4 Use the modified version of do_twice to call print_twice twice, passing 'spam' as an argument.
5 Define a new function called do_four that takes a function object and a value and calls the 
function four times, passing the value as a parameter. There should be only two statements in 
the body of this function, not four.
"""

def print_twice(str_param):
    print str_param
    print str_param


def do_twice(f_function, a_value):
    f_function(a_value)
    f_function(a_value)


def do_four(func_obj, func_value):
    do_twice(func_obj, func_value)
    do_twice(func_obj, func_value)


if __name__ == '__main__':
    do_four(print_twice, 'spam')
    do_twice(print_twice, 'spam')
