class Movie:
    def __init__(self, name=None, minutes=-1, audienceRating='not set'):
        self._name = name
        self._minutes = minutes
        self._audienceRating = audienceRating

    # class property methods - setters & getters
    # def getName(self):
    @property
    def name(self) -> str|None:
        return self._name
    
    # def setName(self, value):
    @name.setter
    def name(self, value:str):
        if not value or not isinstance(value,str):
            raise ValueError

        self._name = value.upper()

    @property
    def minutes(self) -> str|None:
        return self._minutes
    
    @minutes.setter
    def minutes(self, value:int):
        self.setMinutes(value)

    @property
    def audienceRating(self)->str:
        return self._audienceRating

    @audienceRating.setter
    def audienceRating(self, value:str):
        self.setAudienceRating(value)

    # public methods
    def show(self):
        return f"Movie Name: {self.name}\nMovie Duration: {self.minutes} minutes\nMovie Rating: {self.audienceRating}"

    def __str__(self):
        return self.show()
    
    def setMinutes(self, value):
        if not value or not isinstance(value,int):
            raise ValueError
        
        if value < 1:
            raise ValueError
        self._minutes = value

    def setAudienceRating(self, value):
        audienceRating = value.upper()
        availableRatings = ['G', 'PG', 'R13', 'RP13', 'M', 'R15', 'R16', 'RP16', 'R18']
        
        if self._audienceRating == 'not set':
            if value in availableRatings:
                self._audienceRating = audienceRating
                return True
            else:
                raise ValueError
        else:
            raise ValueError
        
        # Code replaced with Pythonic equivalent
        """for availableRating in availableRatings:
            if audienceRating == availableRating:
                self._audienceRating = audienceRating
                return True
        return False"""

    def setNameAndMinutes(self, localname, localminutes):
        if not localname and localminutes or not isinstance(localname and localminutes,int):
            raise ValueError
        
        self.setMinutes(localminutes)
        self.name = localname.upper()
    
if __name__  == "__main__":
    M = Movie()
    M.setNameAndMinutes("the good dinosaur",50)
    M.setAudienceRating("PG")
    print(M)

    
    
