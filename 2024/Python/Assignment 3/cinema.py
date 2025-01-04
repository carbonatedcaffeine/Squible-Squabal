# Camden
from movie import Movie
from booking import Booking
from customer import Customer

class Cinema:
    def __init__(self):
        self._movieDataBase = [
            ["The Shawshank Redemption", 142, "RP16"],
            ["The Godfather", 175, "R16"],
            ["The Dark Knight", 152, "M"],
            ["12 Angry Men", 96, "G"],
            ["Schindler's List", 195, "RP13"],
            ["The Lord of the Rings: The Return of the King", 201, "M"],
            ["One Flew Over the Cuckoo's Nest", 133, "R18"],
            ["The Lord of the Rings: The Fellowship of the Ring", 178, "M"],
            ["Saving Private Ryan", 169, "R15"],
            ["Blade Runner 2049", 164, "R13"],
            ["Halloween", 91, "R16"],
            ["Beverly Hills Cop", 105, "RP16"],
            ["Platoon", 120, "RP16"],
            ["Total Recall", 113, "RP16"],
            ["Back to the Future", 116, "G"],
            ["The Lion King", 88, "G"],
            ["Cars", 117, "G"],
            ["The Wizard of Oz", 102, "G"],
            ["The Wolf of Wall Street", 180, "R18"],
            ["Harry Potter and the Philosopher's Stone", 152, "PG"],
            ["Poltergeist", 114, "PG"],
            ["Full Metal Jacket", 116, "RP13"],
            ["The Exorcist", 122, "R15"],
            ["Apocalypse Now", 147, "R16"],
        ]

        self._movies = []
        self._bookings = []
        self._customers = []

    def addMovie(self,movie:object):
        if not isinstance(movie,Movie):
            raise ValueError
        self._movies.append(movie)

    def addCustomer(self,customer:object):
        if not isinstance(customer,Customer):
            raise ValueError
        self._customers.append(customer)

    def getMovieNames(self):
        for x in range(len(self._movies)):
            print(self._movies[x].name)
    
    def getCustomerNames(self):
        for x in range(len(self._customers)):
            print(self._customers[x].name)

    def remove(self,movieName:str):
        if not movieName or not isinstance(movieName,str):
            raise ValueError
        print(f"-"*25)
        print(f"Searching for movie {movieName.upper()}")
        for x in range(len(self._movies)):
            if self._movies[x].name.upper() == movieName.upper():
                del self._movies[x]
                print(f"Movie {movieName.upper()} found, deleting")
                break
        else:
            print(f"Movie {movieName.upper()} not found")
    
    # Find a movie by using a loop
    def findMovieItem(self,movieName:str):
        if not movieName or not isinstance(movieName,str):
            raise ValueError
        print(f"-"*25)
        print(f"Searching for movie {movieName.upper()}")
        # Loop through until it finds the movie in the list
        for x in range(len(self._movies)):
            if self._movies[x].name.upper() == movieName.upper():
                print(f"Movie {movieName.upper()} found, printing movie info")
                print(f"-"*25)
                print(self._movies[x])
                break
        else:
            print(f"Movie {movieName.upper()} not found")

    def findRatedMoviesNames(self,audienceRating):
        if not audienceRating or not isinstance(audienceRating,str):
            raise ValueError
        print(f"-"*25)
        print(f"Searching for movies with rating {audienceRating}")
        for x in range(len(self._movies)):
            if self._movies[x].audienceRating.upper() == audienceRating.upper():
                print(f"-"*25)
                print(self._movies[x])

    def getTotalMinutes(self):
        sum = 0
        for x in range(len(self._movies)):
            sum += self._movies[x].minutes
        print(f"-"*25)
        print(f"Total minutes of movies: {sum}")

if __name__ == "__main__":
    # Tests
    CI = Cinema()
    M = Movie()
    M2 = Movie()
    C = Customer()
    B = Booking()

    C.name = "Camden"
    C.contactNum = "0283857293"
    C.email = "camden@email.com"
    M.setNameAndMinutes("The Good Dinosaur", 120)
    M.setAudienceRating("PG")
    M2.setNameAndMinutes("The Bad Dinosaur", 120)
    M2.setAudienceRating("R18")
    B.makeBooking(C,3,M,1)
    B.makeBooking(C,4,M,1)

    CI.addMovie(M)
    CI.addMovie(M2)

    for x in CI._movieDataBase:
        CI.addMovie(Movie(x[0].upper(),x[1],x[2]))
        
    
    # First test for printing movies
    #for x in range(len(CI._movies)):
    #    print(f"\nMovie: {x}\n{CI._movies[x]}\n")

    CI.remove("cars")
    CI.findMovieItem("cars")
    CI.findMovieItem("halloween")
    CI.findRatedMoviesNames("r18")
    CI.getTotalMinutes()