# Checking whether any letter of the string is lowercase or not
def any_lowercase1(s):
    for c in s:
        if c.islower():
            return True
        else:
            return False

# Except, empty string it will always return True.
def any_lowercase2(s):
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'

# If last letter of the word is Uppercase, it returns False, for any other thing it returns True
def any_lowercase3(s):
    for c in s:
        flag = c.islower()
    return flag

# Except all letters are uppercase, it will always return True.
def any_lowercase4(s):
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag

# String must have full of lowercase letters. 
def any_lowercase5(s):
    for c in s:
        if not c.islower():
            return False
    return True