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

# Let's use a FreqDist to find the 30 most frequent words of text2 --> Sens