from address import Address

from mailing import Mailing

to_address = Address("142111", "Москва", "ул.Ломоносого", "д.10", "кв.3")

from_address = Address("197733", "Санкт-Петербург", "ул.Пушкина", "д.3", "кв 6")

cost = 2500

track = "№1234567890"

mailing = Mailing(to_address, from_address, cost, track)

print(mailing)