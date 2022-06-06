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


#Exercise 3 - Part 1
def ceaser_encrypt(text):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    shift = 3
    cypher_text = ""
    for letter in text:
        if letter in alphabet:
            index = alphabet.index(letter)
            substitution_index = (index + shift) % len(alphabet)
            cypher_text = cypher_text + alphabet[substitution_index]
        else:
            cypher_text = cypher_text + letter

    return cypher_text


#Exercise 3 - Part 2
def ceaser_decrypt(text):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    shift = 3
    cypher_text = ""
    for letter in text:
        if letter in alphabet:
            index = alphabet.index(letter)
            substitution_index = (index - shift) % len(alphabet)
            cypher_text = cypher_text + alphabet[substitution_index]
        else:
            cypher_text = cypher_text + letter

    return cypher_text