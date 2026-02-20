# Anagram Solver
Simple tool that takes a string input and outputs all valid anagrams from a combined dictionary-thesaurus source.

# Installation
Run 'pip install pandas' into a terminal of your choosing.

# Usage Instructions
Run the tool, wait for the anagram input prompt, type a string and wait for the output list. May take 20-40 seconds.

# How it Works
The tool first creates a pandas dataframe by combining a publicly available thesaurus and dictionary of english words and terms. It then standardises and cleans the compiled list before acquiring the input string. This input is then checked against each term in the dataframe via a Counter function to compare the total number of each character on each side of the comparison. Mismatches get removed from the list, and the final form is then printed as output as long as an anagram was found.

# Example
Anagram to solve: live
Output: {'levi', 'evil', 'veil', 'vile'}

# Limitations
Note that the success of an anagram depends on the dataset of words the program has access to. The current thesaurus + dictionary list is quite exhaustive when it comes to esoteric terms like 'zygophyllaceae' but it won't have plurals like 'cars,' so feel free to experiment with other datasets.