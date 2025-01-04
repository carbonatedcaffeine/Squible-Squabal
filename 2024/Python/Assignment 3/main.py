from cinema import Cinema
from booking import Booking
from customer import Customer
from movie import Movie
from guizero import App, Text, Window, Box, PushButton, ListBox, TitleBox

"""from guizero import App, Text, PushButton, Window, TitleBox, Box

# Guizero stuff goes here
cinemaWindow = App("Cinema Administration",1000,1000,"auto")
cinemaTitle = Text(cinemaWindow,"Cinema Administation",20)
cinemaBox = TitleBox(cinemaWindow,"Wheezer","grid")
cinemaBox2 = Box(cinemaWindow,"grid",align="bottom", width="fill",border=5)
cinemaBox3 = Box(cinemaWindow,"grid",align="left", height="fill",border=5)
push1 = PushButton(cinemaBox2,None,text="Button1",grid=[0,0])
push2 = PushButton(cinemaBox3,None,text="Button2",grid=[1,0])

if __name__ == '__main__':
    cinemaWindow.display()"""

movieDatabase = [
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

customerDatabase = [
    ["Camden","0285445544","camden@email.com"],
    ["Noor","0285445544","noor@email.com"],
    ["John","0285445544","john@email.com"],
    ["Ian","0285445544","ian@email.com"],
    ["Daniel","0285445544","daniel@email.com"],
    ["Ish","0285445544","ish@email.com"],
    ["Graham","0285445544","graham@email.com"],
    ["Seamus","0285445544","seamus@email.com"],
    ["Luan","0285445544","luan@email.com"],
    ["Terrence","0285445544","terrence@email.com"],
]

# Create Cinema and populate databases
focalPoint = Cinema()

for x in movieDatabase:
        focalPoint.addMovie(Movie(x[0].upper(),x[1],x[2]))

for x in customerDatabase:
        focalPoint.addCustomer(Customer(x[0],x[1],x[2]))

if __name__ == "__main__":
    """mainApp = App("Focal Point Cinema Administration",900,500,"auto")
    appTitleText = Text(mainApp,"Focal Point Cinema Administration",24)
    mainAppBox = Box(mainApp,"grid",width="fill",height="fill",border=3)
    ListBox(mainAppBox,focalPoint._movies,width="fill",height="fill",grid=[0,0],scrollbar=True)

    filterBox = Box(mainApp,"auto",width="fill",height="fill",border=3,align="left")
    PushButton(filterBox,align="left",text="not set")
    PushButton(filterBox,align="left",text="G")
    PushButton(filterBox,align="left",text="PG")
    PushButton(filterBox,align="left",text="M")
    PushButton(filterBox,align="left",text="R13")
    PushButton(filterBox,align="left",text="RP13")
    PushButton(filterBox,align="left",text="R15")
    PushButton(filterBox,align="left",text="R16")
    PushButton(filterBox,align="left",text="RP16")
    PushButton(filterBox,align="left",text="R18")
    PushButton(filterBox,align="left",text="all ratings")

    launchBox =TitleBox(mainApp,"WOW","auto",)


    mainApp.display()"""
    while True:
        answerInput = input("> ")
        match answerInput:
              case 'help':
                  print("""
Commands
###########
showmovies: Shows all movies
showcustomers: Shows all customers

                        


""")
                  


# Don't even run this