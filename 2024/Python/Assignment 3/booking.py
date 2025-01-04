from movie import Movie
from customer import Customer
from datetime import datetime
class Booking:
    def __init__(self, bookingid="not set", date=f"{datetime.now().day}-{datetime.now().month}-{datetime.now().year}", acustomer=None, session="not set", movie="not set", seats=1):
        # bookingid format sc (session, customer contact)
        self._bookingid = bookingid
        self._date = date
        self._customer = acustomer
        self._session = session
        self._movie = movie
        self._seats = seats
    
    # bookingid property
    @property
    def bookingid(self):
        return self._bookingid
    
    @bookingid.setter
    def bookingid(self, value):
        print("\nYou cannot do that, a bookingID is generated automatically through the makeBooking method\n")
        raise ValueError
    
    @bookingid.deleter
    def bookingid(self):
        del self._bookingid

    # date property
    @property
    def date(self):
        return self._date
    
    @date.setter
    def date(self, value):
        print("\nYou cannot do that, date is generated automatically\n")
        raise ValueError
    
    @date.deleter
    def date(self):
        del self._date

    # Customer property 
    @property
    def customer(self):
        return self._customer
    
    @customer.setter
    def customer(self, value:str):
        if not isinstance(value,Customer):
            raise ValueError

        self._customer = value
    
    @customer.deleter
    def customer(self):
        del self._customer

    # Session property
    @property
    def session(self):
        return self._session
    
    @session.setter
    def session(self, value:int):
        if not value or not isinstance(value,int):
            raise ValueError
        
        # There are a maximum of up to 4 sessions a day per movie
        # using focal point cinema as a reference.
        if value > 4 or value < 1:
            raise ValueError
        
        self._session = value
    
    @session.deleter
    def session(self):
        del self._session

    # Movie property
    @property
    def movie(self):
        return self._movie
    
    @movie.setter
    def movie(self, value):
        if not isinstance(value,Movie):
            raise ValueError
        self._movie = value

    @movie.deleter
    def movie(self):
        del self._movie

    # Seats property
    @property
    def seats(self):
        return self._seats
    
    @seats.setter
    def seats(self, value:int):
        if not value or not isinstance(value,int):
            raise ValueError
        
        self._seats = value
    
    @seats.deleter
    def seats(self):
        del self._seats

    def makeBooking(self, acustomer, asession, amovie, seats):
        # Leverage the error correction from every class
        # as there is no need to re-write it.
        self.customer = acustomer
        self.movie = amovie
        self.session = asession
        self.seats = seats
        
        # This should be OKAY, as you need to get through everything else to get here. 
        self._bookingid = f"{asession}-{acustomer.contactNum}"

    def editBooking(self, asession:int, aseats:int):
        self.session = asession
        self.seats = aseats

    def deleteBooking(self):
        del self._bookingid
        del self.movie
        del self.session
        del self.seats

    def show(self):
        return f"BookingID: {self.bookingid}\nDate: {self.date}\n\n## Customer Object ##\n{self.customer}\n\n## Movie Object ##\n{self.movie}\n\nSession: {self.session}\nSeats: {self.seats}"

    def __str__(self):
        return self.show()

    # This works, merging into main program    
    #def testBookingid(self,bookingid:str, customer, session):
    #    if bookingid == 'auto':
    #        self._bookingid = f"{session}-{customer.contactNum}"
        
if __name__ == "__main__":
    # Tests
    M = Movie()
    C = Customer()
    B = Booking()
    
    # Example error, as you cannot set bookingid manually.
    # B.bookingid = "hee"

    C.name = "Camden"
    C.contactNum = "0283857293"
    C.email = "camden@email.com"
    M.setNameAndMinutes("The Good Dinosaur", 120)
    M.setAudienceRating("PG")
    B.makeBooking(C,4,M,3)

    print(B)

    B.editBooking(3,3)
    
    print(f"\n####Edited####\n\n{B}")   

    B.deleteBooking()
    print(B)
