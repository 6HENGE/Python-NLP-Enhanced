
""" @SerayBeser

Natural Language Processing with Python

Python ile Dogal Dil Isleme

**** Simple Sentiment Analysis  ****
**** Basit Duygu Analizi ****
"""

from textblob import TextBlob
from textblob.classifiers import NaiveBayesClassifier
from afinn import Afinn


def sentiment_with_TextBlob(text):
    sentiments = list()
    for sentence in text.sentences:
        sentiments.append(sentence.sentiment)
    return sentiments


def sentiment_with_naive_bayes(train, test, text):
    cl = NaiveBayesClassifier(train)
    accuracy_ = cl.accuracy(test)
    class_ = cl.classify(text)
    return accuracy_, class_


def sentiment_affin(text):