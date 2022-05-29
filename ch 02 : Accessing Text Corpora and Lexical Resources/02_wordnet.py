from nltk.corpus import wordnet as wn

print "Synonyms (dog)         : ", wn.synsets('dog')
print "Lemma Names (dog)      : ", wn.synset('dog.n.01').lemma_names()
print "Lemma Definition (dog) : ", wn.synset('dog.n.01').definition()
print "Lemma Examples (dog)   : ", wn.synset('dog.n.01').examples()

dog = wn.synset('dog.n.01')
types_of_dog = dog.hyponyms()
print "Types of Dog           : ", sorted(lemma.name() for synset in types_of_dog for lemma in synset.lemmas())

hypers = dog.hypernyms()
print "Hypernyms (dog)        : ", hypers
print "Root Hypernym (dog)    : ", dog.root_hypernyms()

print "Part Meronyms (dog)    : ", wn.synset('animal.n.01').part_meronyms()
print "Substance Meronyms(dog): ", wn.synset('animal.n.01').substance_meronym