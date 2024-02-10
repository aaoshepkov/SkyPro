phone_number = ''

def set_phone_number(num):
    global phone_number
    phone_number += str(num)

set_phone_number(8)
set_phone_number(8)
set_phone_number(0)
set_phone_number(0)
set_phone_number(5)
set_phone_number(5)
set_phone_number(5)
set_phone_number(3)
set_phone_number(5)
set_phone_number(3)
set_phone_number(5)

print(phone_number, end='')


