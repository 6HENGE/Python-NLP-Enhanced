""" @SerayBeser

Natural Language Processing with Python

Python ile Dogal Dil isleme

**** Word Embeddings (Word2Vec wit GenSim)  ****

Word embedding is the collective name for a set of language modeling
and feature learning techniques in natural language processing (NLP)
where words or phrases from the vocabulary are mapped to vectors of
real numbers. Conceptually it involves a mathematical embedding from
a space with one dimension per word to a continuous vector space with
much lower dimension.
Methods to generate this mapping include neural networks, dimensionality
reduction on the word co-occurrence matrix, probabilistic models, and
explicit representation in terms of the context in which words appear.
Word and phrase embeddings, when used as the underlying input representation,
have been shown to boost the performance in NLP tasks such as syntactic
parsing and sentiment analysis. https://en.wikipedia.org/wiki/Word2vec


Word Embedding Algorithms
1. Embedding Layer
2. Word2Vec :  Word2vec is a group of related models that are used to produce word embeddings.
               Word2Vec kelimeler arasindaki uzakligi vektorel olarak hesaplamayi saglar.
--Continuous Bag-of-Words, or CBOW model.
--Continuous Skip-Gram Model.
3. GloVe


"""
from gensim.models import Word2Vec
from sklearn.decomposition import PCA
from nltk.corpus import gutenberg
from nltk import sent_tokenize
from preprocessing import cleaning_a