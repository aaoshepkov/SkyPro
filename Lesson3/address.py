# class Address:
#     index = 0
#     city = ''
#     street = ''
#     building = 0
#     apartment = 0
#
#     def __init__(self, index, city, street, building, apartment):
#         self.index = index
#         self.city = city
#         self.street = street
#         self.building = building
#         self.apartment = apartment
#
#     def get_address(self):
#         return f'{self.index}, {self.city}, {self.street}, {self.building}, {self.apartment}'
#         #return f'{self.index}, {self.city}, {self.street}, {self.building}, {self.apartment}'
#
#     # def __str__(self):
#     #      return f'{self.index} {self.city} {self.street} {self.building} {self.apartment}'
#
#     #def to_address(self):
#
#         #return f'{self.index} {self.city} {self.street} {self.building} {self.apartment}'
#         #print(self.index, self.city, self.street, self.building, self.apartment, sep=',')
#
#     #def from_address(self):
#         # self.from_address = Address()
#         #return f'{self.index} {self.city} {self.street} {self.building} {self.apartment}'
#         #print(self.index, self.city, self.street, self.building, self.apartment, sep=',')
#
# # new_address = Address('677000', 'Yakutsk', 'Lenina', '5/1', '15')
# #
# # print(new_address.get_address())

class Address:
    def __init__(self, index, city, street, building, apartment):
        self.index = index
        self.city = city
        self.street = street
        self.building = building
        self.apartment = apartment

    def get_address(self):
        return f'{self.index}, {self.city}, {self.street}, {self.building} - {self.apartment}'

    def __str__(self):
        return f'{self.index} {self.city} {self.street} {self.building} {self.apartment}'
