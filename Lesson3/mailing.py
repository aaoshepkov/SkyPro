class Mailing:
    cost = 0
    track = 0

    def __init__(self):
        self.set_address_to = None
        self.set_address_from = None

    def to_address(self, set_address_to, cost, track):
        self.set_address_to = set_address_to
        self.cost = cost
        self.track = track

    def set_from_address(self, set_address_from):
        self.set_address_from = set_address_from

    def new_mailing(self):
        return f'Отправление {self.track} из {self.set_address_from.get_address()} в {self.set_address_to.get_address()}. Стоимость {self.cost} рублей.'

