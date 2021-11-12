""" @SerayBeser

Natural Language Processing with Python
# http://www.nltk.org/book/ch01.html

Python ile Dogal Dil Isleme

"""

# load our data (texts)
# verilerimizi ice aktaralim
# we use text2.
# text2'yi kullanacagiz.
# a frequency distribution could be used to record the frequency of each word type in a document.
# frekans dagilimi, bir belgedeki her bir kelime turunun sikligini kaydetmek icin kullanilabilir.

from nltk.book import text2
from nltk import FreqDist

# Let's use a FreqDist to find the 30 most frequent words of text2 --> Sense and Sensibility by Jane Austen 1811
frequency_distribution = FreqDist(text2)
vocabulary = frequency_distribution.most_common(30)

print "-" * 100
print "Most Common 30 tokens:", vocabulary

print "-" * 100
print "Frequency Distribution word='love' : ", frequency_distribution['love']
print "Frequency Distribution word='hate' : ", frequency_distribution['hate']
print "Frequency Distribution word='sense' : ", frequency_dis