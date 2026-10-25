class User:
    def __init__(self, first_name: str, last_name: str, age: int, gender: str):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender


    def sayName(self):
        print(f'My name is {self.first_name}')

    def sayLast_name(self):
        print(f'My last name is {self.last_name}')

    def sayFull_name(self):
        print(f'My full name is {self.first_name} {self.last_name}')

    def sayAge(self):
        print(f'I`m {self.age} years old')

    def sayGender(self):
        print(f'And I`m a {self.gender}')

