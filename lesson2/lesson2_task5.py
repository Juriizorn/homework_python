num_month = int(input())

def month_to_season(num_month):
    if 1 <= num_month <= 2 or num_month == 12:
        print("Зима")
    elif 3 <= num_month <= 5:
        print("Весна")
    elif 6 <= num_month <= 8:
        print("Лето")
    elif 9 <= num_month <= 11:
        print("Осень")
    else:
        print("Нет такого месяца.")

month_to_season(num_month)