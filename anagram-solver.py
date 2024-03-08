import pandas as pd

# Creating an ordered list of all unique terms from two sources
dictionary = pd.read_csv('dictionary.csv', converters={'Word' : str})
words = list(dictionary['Word'].drop_duplicates())
thesaurus = pd.read_csv('thesaurus.csv', converters={'Word' : str})
words = words + list(thesaurus['Word'].drop_duplicates())
for i in range(len(words)):
    words[i] = words[i].lower()
words.sort()




