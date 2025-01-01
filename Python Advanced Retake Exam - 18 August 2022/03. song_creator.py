def add_songs(*args):
    all_songs = {}
    result = ""

    for song_name, lyrics in args:
        if song_name not in all_songs:
            all_songs[song_name] = []
        for every_lyric in lyrics:
            all_songs[song_name].append(every_lyric)

    for song, lyric in all_songs.items():
        result += f"- {song}\n"
        for l in lyric:
            result += f"{l}\n"

    return result
