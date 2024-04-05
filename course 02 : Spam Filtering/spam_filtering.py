
""" @SerayBeser

Natural Language Processing with Python

Python ile Dogal Dil Isleme

**** Spam Filtering
     Spam Filtreleme ****

dataset : http://www2.aueb.gr/users/ion/data/enron-spam/ : Enron 1
"""
# encoding=utf8
import sys

import warnings
import numpy as np
import collections

from glob import iglob
from nltk.corpus import stopwords
from nltk import word_tokenize
from sklearn.metrics import confusion_matrix
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import LinearSVC
from keras.preprocessing.text import Tokenizer

reload(sys)
sys.setdefaultencoding('utf8')
warnings.filterwarnings('ignore')
stop_words = set(stopwords.words('english'))


def cleaning(text):
    """ cleaning and normalizing data , veri yi temizleme ve normalize etme.
    :param text: raw text
    :return: cleaned and normalized wordlist
    """

    words = [word for word in word_tokenize(str(text)) if word.isalpha()]
    return [w.lower() for w in words]


class Bag_of_Words: