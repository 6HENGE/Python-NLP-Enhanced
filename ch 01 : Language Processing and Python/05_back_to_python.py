""" @SerayBeser

Natural Language Processing with Python
# http://www.nltk.org/book/ch01.html

Python ile Dogal Dil Isleme

"""
# Birkac cumle olusturalim.
# let's create some sentences.

sentence_1 = ['I', 'can', 'not', 'believe', 'how', 'hot', 'it', 'is', 'today', '.']
sentence_2 = ['I', 'like', 'going ', 'out ', 'to', 'parties ', 'with ', 'friends', '.']

print "len(word) < 5  :   ", [w for w in sentence_1 if len(w) < 5]
print "len(word) <= 5 :   ", [w for w in sentence_1 if len(w) <= 5]
print "len(word) == 5 :   ", [w for w in sentence_1 if len(w) == 5]
print "len(word) != 5 :   ", [w for w in sentence_1 if len(w) != 5]
print "-" * 100
print "startswith ('i')  :   ", sorted([w for w in sentence_1 if w.startswith('i')])
print "endswith ('ieve') :   ", sorted([w for w in sentence_1 if w.endswith('ieve')])
pri