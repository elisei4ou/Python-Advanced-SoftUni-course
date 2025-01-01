def forecast(*args):
    weather_towns = {}
    result = ""

    for town, weather in args:

        if weather not in weather_towns.keys():
            weather_towns[weather] = []
        weather_towns[weather].append(town)

    weather_towns = sorted(weather_towns.items(), key=lambda x: (x[0] == 'Rainy', x[0] == "Cloudy", x[0] == "Sunny"))

    for w, t in weather_towns:
        for x in sorted(t):
            result += f"{x} - {w}\n"

    return result

print(forecast(
    ("Beijing", "Sunny"),
    ("Hong Kong", "Rainy"),
    ("Tokyo", "Sunny"),
    ("Sofia", "Cloudy"),
    ("Peru", "Sunny"),
    ("Florence", "Cloudy"),
    ("Bourgas", "Sunny")))


