
movies =[]
def adding():
    title = input("Enter the movie title: ")
    director = input("Enter the movie director: ")
    year = input("Enter the movie release year: ")
    for movie in movies:
        if movie["title"].lower() == title.lower():
            print("Title already exists")
            return
        
    movies.append({
        'title': title,
        'director': director,
        'year': year
    })
        
def listing():
    if not movies:
        print("No Movies Exist")
        return
    
    for movie in movies:
        print(f"Title : {movie["title"]}")
        print(f"Director: {movie["director"]}")
        print(f"Year: {movie["year"]}")


def remove():
    title = input("Enter the title of the movie you want to remove:")
    for movie in movies:
        if movie["title"].lower() == title.lower():
            movies.remove(movie)
            return
        else:
            print("Movie doesnt exist")

show = True
while show:
    u = input("Do you want to proceed:").lower()
    if u == "yes":
        MENU_PROMPT = input("\nEnter 'a' to add a movie, 'l' to see your movies, 'r' to remove a movie: ").lower()
        if MENU_PROMPT == "a":
            adding()
        elif MENU_PROMPT == "l":
            listing()
        else:
            remove()
        print(movies)
    else:
        show = False


