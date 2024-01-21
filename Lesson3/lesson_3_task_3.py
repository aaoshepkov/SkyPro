from address import Address
from mailing import Mailing

set_address_to = Address(112000, 'Moscow', 'Lenina', '5/1', '12')
set_address_from = Address(677000, 'Yakutsk', 'Lenina', '5/1', '12')

new_mailing = Mailing()

new_mailing.to_address(set_address_to, 10, 12345)

new_mailing.set_from_address(set_address_from)

print(new_mailing.new_mailing())
