class Series:
    def __init__(self, title: str, seasons: int, genres: list):
        self.title = title
        self.seasons = seasons
        self.genres = genres
        self.ratings = []

    def __str__(self):
        first_line = f'{self.title} ({self.seasons} seasons)'
        second_line = f'genres: {", ".join(self.genres)}'
        if len(self.ratings) == 0:
            return f'{first_line}\n{second_line}\nno ratings'
        else:
            average = sum(self.ratings) / len(self.ratings)
            return f'{first_line}\n{second_line}\n{len(self.ratings)} ratings, average {average:.1f} points'

    def rate(self, rating: int):
        self.ratings.append(rating)

def minimum_grade(grade: float, series: list):
    min_rating = []
    for series in series:
        average = sum(series.ratings) / len(series.ratings)
        if average >= grade:
            min_rating.append(series)
    return min_rating

def includes_genre(genre: str, series: list):
    genre_list = []
    for series in series:
        if genre in series.genres:
            genre_list.append(series)
    return genre_list