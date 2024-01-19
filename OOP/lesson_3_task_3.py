from address import Address

from mailing import Mailing


to_address = Address('677000', 'Yakutsk', 'Lenin str', '5/1', '11')
from_address = Address('112000', 'Moscow', 'Gorbunova', '2/8', '1132')

new_mailing = Mailing({to_address}, {from_address}, '150', '12345678')
print(new_mailing)