# HOW DO I USE THIS
The "wordsAnalyzer" library runs using python3

First, you have to run the following in terminal if you don't have the libraries:
pip install unidecode
pip install pycountry
pip install bs4
pip install requests
from googlesearch import search

Now, you should be able to import the library as you'd like.

# HOW DO I USE THIS
You can feel free to read through the file, but there are two main functions to keep in mind:

ridAccents(word) -> returns "word" without accents
getCountry(query) -> returns the country most associated with the inputted query

for example:
getCountry("Nintendo") returns "Japan"

# WHAT'S IN DEVELOPMENT
def getContinent(query) -> getCountry(query) but for continents

def getCountryConfidence(query) -> getCountry(query) with confidence value

def getCountryConfidenceFormat(query) -> getCountryConfidence(query) formated for printing

def getInfoConfidence(query) -> a combination of getContinent and getCountryConfidence

# WHAT AM I DOING GOING FORWARD

I'm going to try and add continents measurements as well