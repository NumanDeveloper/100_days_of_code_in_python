# nesting dictionaries inside list
travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
]


def add_new_country(country_visited, times_visited, cities_visited):
    # making a new empty dict and then populating it.
    new_country = {}
    new_country['country'] = country_visited
    new_country['visits'] = times_visited
    new_country['cities'] = cities_visited
    # put in last the newly created dict
    travel_log.append(new_country)


add_new_country("Pakistan", 2, ["Lahore", "Arifwala", "Islamabad"])
print(travel_log)
