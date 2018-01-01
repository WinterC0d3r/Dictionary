"""
English Dictionary, created in python and json. for lightweight use via terminal
"""
import json
import difflib
from difflib import SequenceMatcher
from difflib import get_close_matches

# loading json data file containing Dictionary dataSource
sourceData = json.load(open("DataSource.json"))
# function for searching word
def wordSearch(enteredKey):
    if enteredKey in sourceData:
        return sourceData[enteredKey]
    # incase of typo, getting possible match
    elif len(get_close_matches(enteredKey, sourceData.keys())) > 0:
        return "Did you mean: %s " % get_close_matches(enteredKey, sourceData.keys())[0]
    else:
        return "Word not found, Please recheck"

# input var for lookup
searchInput = input("Enter a word: ")
# printing results
print(wordSearch(searchInput.lower()))
