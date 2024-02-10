class Smartphone:

    def __init__(self, phone_brand, phone_model, abon_number):
        self.brand = phone_brand
        self.model = phone_model
        self.number = abon_number

    def __str__(self):
        return f'{self.brand} - {self.model}. {self.number}'

