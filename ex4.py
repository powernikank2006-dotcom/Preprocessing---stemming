import nltk
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize


nltk.download('punkt')

text = "playing plays played happily running runner runs"

words = word_tokenize(text)

stemmer = PorterStemmer()

stemmed_words = [stemmer.stem(word) for word in words]

print("Original Words :", words)
print("Stemmed Words  :", stemmed_words)
