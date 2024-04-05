
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
    def __init__(self):
        self.corpus = list()
        self.labels = list()
        self.indexes = list()
        self.vocabulary = collections.OrderedDict()

    def create_vocabulary(self, texts):
        """ Updates internal vocabulary based on a list of texts.

        :param texts:
        """
        print "Creating Vocabulary ...",
        self.corpus = cleaning(str(' '.join(texts)).lower())
        self.labels = sorted(set(self.corpus))
        self.indexes = range(0, len(self.labels))
        self.vocabulary = collections.OrderedDict(sorted(dict(zip(self.labels, self.indexes)).items()))
        print "DONE"

    def bag_of_words(self, texts, mode='count'):
        """ Convert a list of texts to a Numpy matrix.

        :param mode:  one of 'binary', 'count', 'freq', default : 'count'
        :param texts: list of sentences
        :return: bag of words (type: numpy ndarray)
        """
        print "Creating Bag of Words ...",
        bows = list()
        count = 0

        for text in texts:
            bow = list()
            text = cleaning(text.lower())
            for v in self.vocabulary:
                if str(mode) == 'count':
                    for t in text:
                        if str(t) == str(v):
                            count += 1
                    bow.append(count)
                    count = 0