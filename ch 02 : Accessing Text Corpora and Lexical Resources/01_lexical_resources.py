""" @SerayBeser

Natural Language Processing with Python
# http://www.nltk.org/book/ch02.html

Python ile Dogal Dil Isleme

"""

"""
A lexicon, or lexical resource, is a collection of words and/or phrases along with associated
information, such as part-of-speech and sense definitions.

Sozcuksel veya sozlu kaynak, sozcuk veya cumlelerin yani sira konusma ve anlam
tanimlarinin bir parcasi gibi iliskili bilgilerden olusan bir derlemedir. 
"""

import nltk


def unusual_words(text):
    text_vocab = set(w.lower() for w in text if w.isalpha())
    english_vocab = set(w.lower() for w in nltk.corpus.words.words())
    unusual = text_vocab - english_vocab
    return sorted(unusual)


def content_f