
""" @SerayBeser

Natural Language Processing with Python

Python ile Dogal Dil Isleme

**** Preprocessing (only words)
 (Manual Cleaning & NLTK cleaning and stemming) ****

"""
from nltk.corpus import gutenberg, stopwords
from nltk import word_tokenize
from nltk.stem.porter import PorterStemmer

import string


def cleaning(text):
    """ CLEANING DATA , veri yi temizleyelim.
    :param text: raw text
    :return: cleaned wordlist
    """
    # 1- Select Only Words, sadece kelimeleri secelim.
    words = str(text).split()

    # 2- Remove Punctuation, noktalama isaretlerini silelim.
    for i in range(0, len(words)):
        for punct in string.punctuation:
            if str(punct) in words[i]:
                words[i] = str(words[i]).replace(str(punct), ' ')

    # 3- Normalizing Case, buyuk kucuk harf normalizasyonunu yapalim.
    words = [w.lower() for w in words]

    # 4- Remove StopWords, stopwords leri kaldiralim.
    stop_words = ['a', 'about', 'above', 'across', 'after', 'afterwards']
    stop_words += ['again', 'against', 'all', 'almost', 'alone', 'along']
    stop_words += ['already', 'also', 'although', 'always', 'am', 'among']
    stop_words += ['amongst', 'amoungst', 'amount', 'an', 'and', 'another']
    stop_words += ['any', 'anyhow', 'anyone', 'anything', 'anyway', 'anywhere']
    stop_words += ['are', 'around', 'as', 'at', 'back', 'be', 'became']
    stop_words += ['because', 'become', 'becomes', 'becoming', 'been']
    stop_words += ['before', 'beforehand', 'behind', 'being', 'below']
    stop_words += ['beside', 'besides', 'between', 'beyond', 'bill', 'both']
    stop_words += ['bottom', 'but', 'by', 'call', 'can', 'cannot', 'cant']
    stop_words += ['co', 'computer', 'con', 'could', 'couldnt', 'cry', 'de']
    stop_words += ['describe', 'detail', 'did', 'do', 'done', 'down', 'due']
    stop_words += ['during', 'each', 'eg', 'eight', 'either', 'eleven', 'else']
    stop_words += ['elsewhere', 'empty', 'enough', 'etc', 'even', 'ever']
    stop_words += ['every', 'everyone', 'everything', 'everywhere', 'except']