import unidecode
import pycountry
import bs4
import requests
from googlesearch import search

# this library allows for work with words!!!


# let's start by building a database of countries...

def buildCountries():
    tmp = []
    for country in pycountry.countries:
        tmp.append(country.name)
    
    return tmp

continents = {"Antarctica", "North America", "South America", "Asia", "Europe", "Africa"}
# ok...


# FUNCTIONS :)


# let's start with something simple:
# a function that gets rid of accents in a word, best it can
def ridAccents(word):
    return unidecode.unidecode(accented_string)


# alright, now let's get some information about the google search results
# for a word!
# return values: [links, google_html, links_html]
def getGoogleResults(query):
    links = []
    # from geeks4geeks
    print("Getting google results...")
    for j in search(query, tld="co.in", num=10, stop=10, pause=2):
        links.append(j)
    print("Got google results!")
    
    # now, let's get the html for the google search page!
    print("Getting google html...")
    google_html = requests.get("https://www.google.com/search?q=" + query).text
    print("Got google html!")
    # let's also get the HTML page of each subsequent result!
    links_html = []
    print("Getting html from links...")
    counter = 0
    for link in links:
        print("Getting html for link {0}".format(counter + 1))
        try:
            links_html.append(requests.get(link).text)
        except:
            print("Couldn't get this page, moving on...")
            continue
        counter += 1

    print("Got html from links!")
    
    return [links, google_html, links_html]


# awesome!
# but what if we want to find out where something is from????
# let's create a new function, called countCountries, that creates a hash
# to count how many times a country is found in a string!

def safeSearch(word, string):
    tmp = 0
    wordVariants = [word, word.lower(), word.upper()]
    fullWordVariants = []
    for w in wordVariants:
        fullWordVariants.append(" " + w)
        fullWordVariants.append(" " + w + " ")
        fullWordVariants.append(" " + w + ".")
        fullWordVariants.append(" " + w + "!")
        fullWordVariants.append(" " + w + ",")
        fullWordVariants.append(" " + w + ":")
        fullWordVariants.append(" " + w + ";")
    for w in fullWordVariants:
        tmp += string.count(w)
    
    return tmp

# returns hash of how many times items of "lst" appear in search results of "query"
def countWithin(query, lst):
    x = getGoogleResults(query)
    gResults, pResults = x[1], x[2]
    hashCounter = {}
    print("Creating hash...")
    for item in lst:
        tmp = 0
        counter = 1
        print("Going through google results...")
        tmp += safeSearch(item, gResults)
        for result in pResults:
            print("Going through link {0}".format(counter))
            tmp += safeSearch(item, result)
            counter += 1
        hashCounter[item] = tmp
    return hashCounter

# now, let's rank the hash and create a function that
# takes a query and returns the best guess for the place
# of origin!
# returns: country w results, total countries found, entire hash
def getCountry(query):
    h = countWithin(query, buildCountries())
    print("Sorting list...")
    lst = sorted(h.items(), key = lambda x : x[1], reverse = True)
    print("List sorted!")
    print("Country approx: {0}".format(lst[0]))
    return lst[0], sum(h.values()), lst

# some new functions!!!!!!

# TODO: Gets Continent Ranking!
def getContinent(query):
    x = 1

# TODO: Produces confidence result of query
# EX) getCountryConfidence("Nintendo") -> ["Japan", 1.0]
def getCountryConfidence(query):
    countryInfo, sumOfCountries, countriesFinal = getCountry(query)
    country = countryInfo[0]
    countryCount = countryInfo[1]

    print("{0} appeared a total of {1} times out of {2} country finds".format(country, countryCount, sumOfCountries))
    print("This is a confidence of {0}".format(round(countryCount/sumOfCountries, 4)))
    print("\nCompare this with the second most: {0} with {1}".format(countriesFinal[1][0], countriesFinal[1][1]))

# if confidence is >= 0.9, then it just returns the country
def getCountryConfidenceFormat(query):
    x = 1

# TODO: Gets hash of continent and country
# EX) getInfoConfidence("Nintendo") -> {"continent" : Asia,
#                                        "Country" : ["Japan", 1.0]}
def getInfoConfidence(query):
    x = 1