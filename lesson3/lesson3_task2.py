from smartphone import Smartphone

catalog = [
    Smartphone("Honor", "400 Pro","+79334445566"),
    Smartphone("Honor", "X9c", "+79445556677"),
    Smartphone("Samsung", "Galaxy S25 FE", "+79556667788"),
    Smartphone("Samsung", "Galaxy Z Flip7", "+79112223344"),
    Smartphone("Apple", "iPhone 17 Pro", "+79223334455")
]

for Smartphone in catalog:
    print(f"{Smartphone.phone_brand} - {Smartphone.phone_model}. {Smartphone.phone_number}")