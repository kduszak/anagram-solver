import pandas as pd
import re
from collections import Counter

# Creating an ordered list of all unique terms from two sources
dictionary = pd.read_csv('dictionary.csv', converters={'Word' : str})
words = list(dictionary['Word'].drop_duplicates())
thesaurus = pd.read_csv('thesaurus.csv', converters={'Word' : str})
words = words + list(thesaurus['Word'].drop_duplicates())
words_length = len(words)
      
for i in range(words_length):
    words[i] = words[i].lower()

#todo: turn list unique here
words.sort()


term = input("Anagram to solve: ")
term_length = len(term)

#Cutting all wrong-length words from list
i = 0
while i < words_length:
    if (len(words[i]) != term_length):
        words.remove(words[i])
        words_length -= 1
    else:
        i += 1

i = 0
j = 0
while i < words_length:
    j = 0
    success = True
    #print("i: " + str(i))
    #print("words_length: " + str(words_length))
    while j < term_length and i < words_length:
        #if (re.search("^.*" + term[j] + ".*$", words[i]) and (re.search("^.*" + words[i][j] + ".*$", term))):
        if Counter(term) == Counter(words[i]):
            j+=1
            #print(words[i] + " " + str(j + 1) + "/" + str(term_length))
            #print(words[i] + " contains '" + term[j] + "'")
        else:
            words.remove(words[i])
            words_length -= 1
            success = False
    if success:
        i += 1


words = set(words)
if term in words:
    words.remove(term)
words_length = len(words)
if (words_length > 0):
    print(words)
else:
    print("No anagrams found")






