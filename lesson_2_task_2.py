def is_year_leap(num):
    entered_year = num
    if num % 4 == 0:
        print('год', entered_year, ':', 'True')
    else:
        print('год', entered_year, ':', 'False')
is_year_leap(2024)


# number = int(input('Введите год: '))
# def is_year_leap1():
#     global number
#     if number % 4 == 0:
#         print('год', entered_year, ':', 'True')
#     else:
#         print('год', entered_year, ':', 'False')
# is_year_leap1()
