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
        varValidate = input ("Did you mean: %s\nType \"Y\" for yes, \"N\" for no. " % get_close_matches(enteredKey, sourceData.keys())[0])

        #input validation
        if varValidate == "Y":
            return sourceData[get_close_matches(enteredKey, sourceData.keys())[0]]
        elif varValidate == 'N':
            return "Did not find a match"
        else:
            return "You did not select a valid option"
    else:
        return "Word not found, Please recheck...."

# input var for search
searchInput = input("Enter a word: ")

# storing output into a variable for optimization
results = wordSearch(searchInput.lower())
if type(results) == list:
    for r in results:
        print(r)
else:
    print(restults)
