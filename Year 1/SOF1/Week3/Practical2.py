import string
import re

#Exercise 1
def is_palindrome(text):
    text_stripped = text.translate(str.maketrans('', '', string.punctuation)).lower().replace(" ", "")
    reversed = text_stripped[::-1]
    print(text_stripped)
    if reversed == text_stripped:
        return True
    else:
        return False


#Exercise 2 - Part 1 and 2
def space_and_camel_case(text):
    text_new = string.capwords(text)
    text_final = text_new.replace(" ", "")
    return text_final


#Exercise 2 - Part 3
def split_camel_case(text):
    return re.findall('[A-Z][^A-Z]*', text)


#Exercise 3