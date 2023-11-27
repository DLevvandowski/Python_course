# Ex. 6.11 Cities
# Create a dictionary named cities. Provide the names of three cities as keys. For each city, create a separate
# dictionary containing information about the city, such as the country in which the city is located, the approximate
# population and some fact from the history of the city. So the keys of the dictionary containing information about the
# city could be 'country', 'population' and 'fact'. Display the name of each city and all the information collected
# about it.

cities = {
    'los angeles': {
        'country': 'usa',
        'population': '3,849 mln',
        'fact': 'originally, the "hollywood" sign read "hollywoodland" and was an advertisement for houses built on '
                'the hills above.',
        },
    'london': {
        'country': 'england',
        'population': '8,982 mln',
        'fact': 'London black cab drivers have to learn street names and local maps for up to four years before they '
                'can take the exam and get certified to drive cabs.',
        },
    'new york': {
        'country': 'usa',
        'population': '8,468 mln',
        'fact': 'New York is otherwise known as The Big Apple and is three times the size of Poland.',
        },
    }

for city, city_info in cities.items():
    print(f"\nSome information about {city.title()}:")
    country = city_info['country']
    population = city_info['population']
    fact = city_info['fact']

    if country == 'usa':
        print(f"\tCountry: {country.upper()}")
    else:
        print(f"\tCountry: {country.title()}")
    print(f"\tPopulation: {population}\n"
          f"\tFact: {fact}")
