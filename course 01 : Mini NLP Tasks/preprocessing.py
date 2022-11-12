
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
    stop_words += ['few', 'fifteen', 'fifty', 'fill', 'find', 'fire', 'first']
    stop_words += ['five', 'for', 'former', 'formerly', 'forty', 'found']
    stop_words += ['four', 'from', 'front', 'full', 'further', 'get', 'give']
    stop_words += ['go', 'had', 'has', 'hasnt', 'have', 'he', 'hence', 'her']
    stop_words += ['here', 'hereafter', 'hereby', 'herein', 'hereupon', 'hers']
    stop_words += ['herself', 'him', 'himself', 'his', 'how', 'however']
    stop_words += ['hundred', 'i', 'ie', 'if', 'in', 'inc', 'indeed']
    stop_words += ['interest', 'into', 'is', 'it', 'its', 'itself', 'keep']
    stop_words += ['last', 'latter', 'latterly', 'least', 'less', 'ltd', 'made']
    stop_words += ['many', 'may', 'me', 'meanwhile', 'might', 'mill', 'mine']
    stop_words += ['more', 'moreover', 'most', 'mostly', 'move', 'much']
    stop_words += ['must', 'my', 'myself', 'name', 'namely', 'neither', 'never']
    stop_words += ['nevertheless', 'next', 'nine', 'no', 'nobody', 'none']
    stop_words += ['noone', 'nor', 'not', 'nothing', 'now', 'nowhere', 'of']
    stop_words += ['off', 'often', 'on', 'once', 'one', 'only', 'onto', 'or']
    stop_words += ['other', 'others', 'otherwise', 'our', 'ours', 'ourselves']
    stop_words += ['out', 'over', 'own', 'part', 'per', 'perhaps', 'please']
    stop_words += ['put', 'rather', 're', 's', 'same', 'see', 'seem', 'seemed']
    stop_words += ['seeming', 'seems', 'serious', 'several', 'she', 'should']
    stop_words += ['show', 'side', 'since', 'sincere', 'six', 'sixty', 'so']
    stop_words += ['some', 'somehow', 'someone', 'something', 'sometime']
    stop_words += ['sometimes', 'somewhere', 'still', 'such', 'system', 'take']
    stop_words += ['ten', 'than', 'that', 'the', 'their', 'them', 'themselves']