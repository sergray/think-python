def find(word, letter, start):
    index = start - 1
    while index < len(word):
        if word[index] == letter:
            return index + 1 # the place of letter
        index = index + 1
    return -1


print find("ahmet", "m", 3)