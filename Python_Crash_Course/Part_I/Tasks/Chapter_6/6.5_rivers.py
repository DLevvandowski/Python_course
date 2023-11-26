# Ex. 6.5 Rivers
# Create a dictionary containing three important rivers and the countries through which they flow. One of the key-value
# pairs can be 'nil': 'egypt'.
# » Use a loop to display a sentence about each river, for example: "The Nile flows through Egypt."
# » Use the loop to display the names of all the rivers stored in the dictionary.
# » Use the loop to display the names of all countries stored in the dictionary.

rivers_and_countries = {
    'nile': 'egypt',
    'amazon': 'brasil',
    'yangtze': 'china',
    }

for river, country in rivers_and_countries.items():
    print(f"The {river.title()} flows through {country.title()}.")

print("\nRivers:")
for river in rivers_and_countries.keys():
    print(river.title())

print('\nCountries:')
for country in rivers_and_countries.values():
    print(country.title())
