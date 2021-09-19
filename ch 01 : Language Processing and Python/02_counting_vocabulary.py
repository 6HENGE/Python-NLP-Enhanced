
""" @SerayBeser

Natural Language Processing with Python
# http://www.nltk.org/book/ch01.html

Python ile Dogal Dil Isleme

"""

# load our data (texts)
# verilerimizi ice aktaralim

from nltk.book import text2

# we use text2.
# text2'yi kullanacagiz.

# len : Return the number of items of a sequence or collection.
# len : text'in uzunlugunu yani karakter sayisini doner
print "-" * 100
print "Number of Words and Punctuation Symbols(Tokens), (Kelime, Noktalama Sayisi):", len(text2)

# tokens : sequence of str
# tokens : text deki kelimelerin listesi

# set of words (distinct words)
# text deki tum kelimeler
print "-" * 100
print "Set of Words (Kelimeler):", set(text2)

# sorted set of words