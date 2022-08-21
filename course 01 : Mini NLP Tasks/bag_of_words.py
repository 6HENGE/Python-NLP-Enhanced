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
    X = vectorizer.fit_transform(te