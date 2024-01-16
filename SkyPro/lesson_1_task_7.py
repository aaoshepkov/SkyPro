number = ''
def phone_number(num):
    global number
    num = str(num)
    number = number + num

phone_number(8)
phone_number(8)
phone_number(0)
phone_number(0)
phone_number(5)
phone_number(5)
phone_number(5)
phone_number(3)
phone_number(5)
phone_number(3)
phone_number(5)

print(number)