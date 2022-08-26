import string
import random

def load_words():
    """
    Ye function kaafi jayada words ko load karne mai help karega
    """
    word_list = ["navgurukul", "learning", "kindness"]
    return word_list
def choose_word():
    """
    word_list (list): list of words (strings)
    ye function ek word randomly return karega
    """
    q=load_words()
    secret_word = random.choice(q)
    secret_word = secret_word.lower()

    return secret_word
a=choose_word()
print(a)
# print(a)
