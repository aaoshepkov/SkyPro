class Address:
    index = 0
    city = ''
    street = ''
    building = 0
    appartment = 0
    def __init__(self, index, city, street, building, appartment):
        self.index = index
        self.city = city
        self.street = street
        self.building = building
        self.appartment = appartment

    # def __str__(self):
    #      return f'{self.index} {self.city} {self.street} {self.building} {self.appartment}'

    def to_address(self):
        return f'{self.index} {self.city} {self.street} {self.building} {self.appartment}'

    def from_address(self):
        #self.from_address = Address()
        return f'{self.index} {self.city} {self.street} {self.building} {self.appartment}'

    from_address()