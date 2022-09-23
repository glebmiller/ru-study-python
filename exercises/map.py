from typing import Union


class MapExercise:
    @staticmethod
    def rating(list_of_movies: list[dict]) -> float:
        def positive_rating(movie: dict) -> float:
            if movie["rating_kinopoisk"] == "":
                movie["rating_kinopoisk"] = 0
            else:
                movie["rating_kinopoisk"] = float(movie["rating_kinopoisk"])

            if "," in movie["country"] and movie["rating_kinopoisk"] != (0.0):
                return float(movie["rating_kinopoisk"])
            else:
                return None

        list_of_floats = list(map(positive_rating, list_of_movies))
        list_of_floats_filtered = list(filter(lambda x: x is not None, list_of_floats))
        return sum(list_of_floats_filtered) / len(list_of_floats_filtered)

    @staticmethod
    def chars_count(list_of_movies: list[dict], rating: Union[float, int]) -> int:
        def count_i(movie: dict) -> int:
            if movie["rating_kinopoisk"] != "" and float(movie["rating_kinopoisk"]) > rating:
                return movie["name"].count("и")
            else:
                return 0

        list_of_letter_counts = map(count_i, list_of_movies)
        return sum(list_of_letter_counts)
