# Nesting       = něco v něčem

cities = {
    "Spain": "Madrid",
    "France": "Paris"
}
# print(cities["Spain"])      # chci ten to key, tak se vypíše value

# # list v dictionary:
# travel_diary = {
#     "Spain": ["Madrid", "Leon", "Valencia"],
#     "France": ["Paris", "Nice", "Rennes"]
# }

# print(travel_diary["France"][0])        # v dictionary vidím slovník a indexem ho najdu - Paris je v listu na indexu 0!

# dictionary v dictionary:
# travel_diary = {
#     "Spain": {"visited_cities": ["Madrid", "Leon", "Valencia"], "visits": 5},
#     "France": {"visited_cities": ["Paris", "Nice", "Rennes"], "visits": 2}
# }

# print(travel_diary["France"]["visited_cities"][1])  # slovník ve slovníku

# dictionary v listu:
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

# musím si vždy uvědomit, že list je přes indexy a slovník přes keys!!
print(travel_diary[0]["visited_cities"][0])

