"""
English Dictionary, created in python and json. for lightweigh use via terminal
"""
import json
# loading json data file containing Dictionary dataSource
sourceData = json.load(open("DataSource.json"))
def wordSearch(enterKey):
    return sourceData[enterKey]

# input var for lookup
searchInput = input("Enter a word: ")
# printing results
print(wordSearch(searchInput.lower()))
