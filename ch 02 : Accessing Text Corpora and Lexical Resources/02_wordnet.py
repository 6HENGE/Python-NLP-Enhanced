from nltk.corpus import wordnet as wn

print "Synonyms (dog)         : ", wn.synsets('dog')
print "Lemma Names (dog)      : ", wn.synset('dog.n.01').lemma_names()
print "Lemma Definition (dog) : ", wn.