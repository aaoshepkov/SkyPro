
from address import Address
class Mailing:
    to_address = Address.to_address
    from_address = Address.from_address

    def __init__(self, to_address, from_address, cost, track):
        self.to_address = to_address
        self.from_address = from_address
        self.cost = cost
        self.track = track


        print('Address entered')

    def __str__(self):
        return f'Отправление {self.track} из {self.from_address}. Цена {self.cost}. Track-number {self.track}'

# new_mailing = Mailing('Moscow', 'New-York', '10', '12345678')
# print(new_mailing)