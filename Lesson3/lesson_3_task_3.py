from address import Address
from mailing import Mailing

set_address_to = Address(108849, 'Москва', 'Льва Кассиля', '1к2', '58')
set_address_from = Address(677008, 'Якутск', 'Лермонтова', '96/1', '55')

new_mailing = Mailing()

new_mailing.to_address(set_address_to, 10, '№1')

new_mailing.set_from_address(set_address_from)

print(new_mailing.new_mailing())
