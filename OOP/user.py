class User:


    def __init__(self, first_name, last_name):
        print('Я создался')
        self.username1 = first_name
        self.username2 = last_name


    def say_first_name(self):
        print('Меня зовут', self.username1)
    #
    def say_last_name(self):
        print('Моя фамилия', self.username2)
    #
    def say_full_name(self):
        print('Мое полное имя', self.username1, self.username2)


# alex = User('Alex', 'Bond')
# mark = User('Mark', 'Aurelius')
# mila = User('Mila', 'Jovovic')
# alex.say_first_name()
# alex.say_last_name()
# alex.say_full_name()
# mark.say_first_name()
# mark.say_last_name()
# mark.say_full_name()
# mila.say_first_name()
# mila.say_last_name()
# mila.say_full_name()
