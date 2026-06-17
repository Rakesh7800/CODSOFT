media_library = {
    "Interstellar": ["Sci-Fi", "Drama", "Mystery"],
    "Inception": ["Sci-Fi", "Action", "Thriller"],
    "The Dark Knight": ["Action", "Crime", "Drama"],
    "The Social Network": ["Drama", "Biography"],
}

def fetch_recommendations(preferred_genre):
    matches = []
    for title, genres in media_library.items():
        if preferred_genre.capitalize() in genres:
            matches.append(title)
    return matches

target_genre = input("Specify your preferred genre: ")
suggestions = fetch_recommendations(target_genre)

if suggestions:
    print(f"Recommendations aligned with '{target_genre}':")
    for movie in suggestions:
        print(f"* {movie}")
else:
    print("Zero matches found for this genre in the local repository.")

