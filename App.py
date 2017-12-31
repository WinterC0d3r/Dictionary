"""
English Dictionary, created in python and json. for lightweigh use via terminal
"""
import json
import difflib
from difflib import SequenceMatcher
from difflib import get_close_matches

# loading json data file containing Dictionary dataSource
sourceData = json.load(open("DataSource.json"))
def wordSearch(enterKey):
    if enterKey in sourceData:
        return sourceData[enterKey]
    else:
        return "Word no found, Please recheck"
        
# input var for lookup
searchInput = input("Enter a word: ")
# printing results
print(wordSearch(searchInput.lower()))
