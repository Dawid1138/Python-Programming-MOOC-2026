def find_movies(database: list, search_term: str):
    new_database = []
    search_term = search_term.lower()
    
    for movie in database:
        if search_term in movie["name"].lower():
            new_database.append(movie)
            
    return new_database