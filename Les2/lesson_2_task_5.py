month_to_season = int(input("Введите месяц для определения сезона: "))

if (month_to_season == 1) or (month_to_season == 2) or (month_to_season == 12):
    print("Зима")
elif (month_to_season == 3) or (month_to_season == 4) or (month_to_season == 5):
    print("Весна")
elif (month_to_season == 6) or (month_to_season == 7) or (month_to_season == 8):
    print("Лето")
elif (month_to_season == 9) or (month_to_season == 10) or (month_to_season == 11):
    print("Осень")
elif(month_to_season < 1):
    print("Шутник чтоли!")
elif (month_to_season > 12):
    print("Такого месяца нет")