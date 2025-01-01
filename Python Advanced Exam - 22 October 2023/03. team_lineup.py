def team_lineup(*args):
    countries = {}
    result = ""

    for player, countrie in args:

        if countrie not in countries.keys():
            countries[countrie] = []
        countries[countrie].append(player)

    countries = sorted(countries.items(), key=lambda x: (-len(x[1]), x[0]))

    for country_name, player_names in countries:
        result += f"{country_name}:\n"
        for every_p in player_names:
            result += f"  -{every_p}\n"

    return result


print(team_lineup(
    ("Harry Kane", "England"),
    ("Manuel Neuer", "Germany"),
    ("Raheem Sterling", "England"),
    ("Toni Kroos", "Germany"),
    ("Cristiano Ronaldo", "Portugal"),
    ("Thomas Muller", "Germany")))