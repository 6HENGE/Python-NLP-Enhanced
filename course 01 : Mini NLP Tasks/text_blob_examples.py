from textblob import TextBlob, Word

text = TextBlob("John likes to watch movies. Mary likes movies too. These are amazing movies. ")

print "Tags            : ", text.tags  # nltk -> pos_tag
print "No