import datetime as dt

class User():
    def __init__(self,id: int, firstName: str, lastName: str, dateAdded: dt):
        self.id = id
        self.firstName = firstName
        self.lastName = lastName
        self.dateAdded = dateAdded

    def outputFields(self):
        fields = (self.id, self.firstName,self.lastName,self.dateAdded)
        return fields