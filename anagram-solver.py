import pandas as pd

# Creating a list of all unique words
dictionary = pd.read_csv('dictionary.csv', keep_default_na = False, na_values = ['NaN'])
words = list(dictionary['Word'].drop_duplicates())