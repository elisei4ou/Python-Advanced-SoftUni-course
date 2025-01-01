def movie_organizer(*args):
    my_movies = {}
    result = ""

    for movie in args:
        name, genre = movie

        if genre not  in my_movies.keys():
            my_movies[genre] = []
        my_movies[genre].append(name)

    my_movies = sorted(my_movies.items(), key=lambda x: (-len(x[1]), x[0]))

    for g, m in my_movies:
        result += f"{g} - {len(m)}\n"

        for e_m in sorted(m):
            result += f"* {e_m}\n"

    return result

print(movie_organizer(
    ("Avatar: The Way of Water", "Action"),
    ("House Of Gucci", "Drama"),
    ("Top Gun", "Action"),
    ("Ted", "Comedy"),
    ("Duck Soup", "Comedy"),
    ("The Dark Knight", "Action"),
    ("A Star Is Born", "Musicals"),
    ("The Warrior", "Action"),
    ("Like A Boss", "Comedy"),
    ("The Green Mile", "Drama"),
    ("21 Jump Street", "Comedy")))

