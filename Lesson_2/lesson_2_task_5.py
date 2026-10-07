def month_to_season(num_month):
    # можно было бы перечислить конкретно (num_month == 12 or..num_month== 2)
    # но так короче
    if num_month in (12, 1, 2):
        print('Зима')
    elif num_month in (3, 4, 5):
        print('Весна')
    elif num_month in (6, 7, 8):
        print('Лето')
    elif num_month in (9, 10, 11):
        print('Осень')
    # ну и обязательно проверяем, чтобы ввели корректный месяц
    else:
        print('Введен некорректный номер месяца')


num = int(input('Введите, пожалуйста, номер месяца(от 1 до 12): '))
month_to_season(num)
