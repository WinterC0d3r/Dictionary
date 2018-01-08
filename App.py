"""
English Dictionary, created in python and json. for lightweight use via terminal
"""
import json
from difflib import get_close_matches

# loading json data file containing Dictionary dataSource
sourceData = json.load(open("DataSource.json"))

# function for searching word
def wordSearch(enteredKey):
    enteredKey = enteredKey.lower()
    if enteredKey in sourceData:
        return sourceData[enteredKey]
    # if the entered word is a noun for e.g. a place name
    elif enteredKey.title() in sourceData:
        return sourceData[enteredKey.title()]
    # for acronyms search
    elif enteredKey.upper() in sourceData:
        return sourceData[enteredKey.upper()]
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
results = wordSearch(searchInput)
if type(results) == list:
    for r in results:
        print(r)
else:
    print(results)
