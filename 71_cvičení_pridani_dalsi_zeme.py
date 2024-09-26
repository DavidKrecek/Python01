travel_diary = [
    {
        "country": "Spain",
        "visited_cities": ["Madrid", "Leon", "Valencia"],
        "visits": 5
    },
    {
        "country": "France",
        "visited_cities": ["Paris", "Nice", "Rennes"],
        "visits": 2
    }
]

def add_country(country_name, towns_list, visits_number):
    new_dictionary = {}
    new_dictionary["Country"] = country_name
    new_dictionary["visited_cities"] = towns_list
    new_dictionary["visits"] = visits_number
    travel_diary.append(new_dictionary)

add_country("Italy", ["Rome", "Florence", "Milan"], 9)
print(travel_diary)

# konkrétní výpis návštěv 9:
print(travel_diary[2]["visits"])