from address import Address

class Mailing:

    def __init__(self, to_address: Address, from_address: Address, cost: int, track: str):
        self.to_address = to_address
        self.from_address = from_address
        self.cost = cost
        self.track = track

    def __str__(self):
        return (f"Отправление {self.track} из {self.to_address.index}, {self.to_address.city},"
                f" {self.to_address.streets}, {self.to_address.house} - {self.to_address.apartment}"
                f" в {self.from_address.index}, {self.from_address.city}, {self.from_address.streets}, "
                f"{self.from_address.house} - {self.from_address.apartment}. Стоимость {self.cost} рублей.")

