class Customer:
    def __init__(self, aname=None, contactNum="0", email=None):
        self._name = aname
        self._contactNum = contactNum
        self._email = email
    
    # Name property 
    @property
    def name(self):
        #print("Getting name!")
        return self._name
    
    @name.setter
    def name(self, value:str):
        if not value or not isinstance(value,str):
            raise ValueError
        
        #print(f'Setting name to "{value}".')
        self._name = value

    # Contact property
    @property
    def contactNum(self):
        #print("Getting contact!")
        return self._contactNum
    
    @contactNum.setter
    def contactNum(self, value:str):
        if not value or not isinstance(value,str):
            raise ValueError
        if len(value) < 9 or len(value) > 12:
            raise ValueError
        
        #print(f'Setting contactNum to "{value}".')
        self._contactNum = value

    # Email property
    @property
    def email(self):
        #print("Getting email!")
        return self._email
    
    @email.setter
    def email(self, value:str):
        if not value or not isinstance(value,str):
            raise ValueError
        #print(f'Setting email to "{value}".')
        self._email = value

    def show(self):
        return f"Name: {self.name}\nContact Number: {self.contactNum}\nEmail: {self.email}"

    def __str__(self):
        return self.show()

if __name__ == "__main__":
    # Tests
    C = Customer()
    C.name = "Camden"
    C.contactNum = "028111111"
    C.email = "camden@email.com"
    print(C)