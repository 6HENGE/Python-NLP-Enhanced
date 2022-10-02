""" @SerayBeser

Natural Language Processing with Python

Python ile Dogal Dil Isleme

**** Bag Of Words ****

Bag of Words (BoW) is a model used in natural language processing.
One aim of BoW is to categorize documents.
The idea is to analyse and classify different "bags of words" (corpus).
And by matching the different categories, we identify which "bag" a certain block of text (test data) comes from.
https://ongspxm.github.io/blog/2014/12/bag-of-words-natural-language-processing/

Building a "Bag of Words" involves 3 steps:
Kelime Cantasi olusturma 3 asamalidir:

--tokenizing
--counting
--normalizing

Kelime Cantasi- (Bag of Words) (BoW), dogal dil islemesinde kullanilan bir modeldir.
BoW'un bir amaci, belgeleri kategorize etmektir. Amac farkli "canta sozcukleri" 'ni (korpus)
analiz etmek ve siniflandirmaktir. Farkli kategorilere eslestirerek,
belirli bir metin blogunun (test verisi) "cantasini" tanimlamis oluyoruz.
"""
from sklearn.feature_extraction.text import CountVectorizer
from preprocessing import cleaning_and_stemming
import collections
import numpy as np


def bag_of_words_with_scikit_learn(texts):
    """

    :param texts: list of sentences
    :return: bag of words (type: numpy ndarray)
    """
    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(texts)
    return X.toarray()


def bag_of_words(texts, mode='count'):
    """

    :param mode:  one of 'binary', 'count', 'freq', default : 'count'
    :param texts: list of sentences
    :return: bag of words (type: numpy ndarray)
    """
    corpus = cleaning_and_stemming(str(' '.join(texts)).lower(), stemming=False, stopword=False)
    labels = sorted(set(corpus))
    indexes = range(0, len(labels))
    vocabulary = collections.OrderedDict(sorted(dict(zip(labels, indexes)).items()))

    bows = list()
    count = 0

    for text in texts:
        bow = list()
        text = cleaning_and_stemming(text.lower(), stemming=False, stopword=False)
        for v in vocabulary:
            if str(mode) == 'count':
                for t in text:
                    if str(t) == str(v):
                        count += 1
                bow.append(count)
    