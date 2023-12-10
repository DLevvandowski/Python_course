# Ex. 8.5 Cities
# Create a function called describe_city(), accepting the name of a city and a country. This function should display a
# simple sentence, such as "Warsaw is in Poland." Assign a default value to the parameter storing the country name. Call
# the prepared function for three different cities, at least one of which should not be located in the default defined
# country.

def describe_city(city, country="italy"):
    print(f"\n{city.title()} is in {country.title()}.")

describe_city('rome')
describe_city('venice')
describe_city('paris')
