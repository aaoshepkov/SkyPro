def number():
    for _ in range(11):
        num = int(input('Введите число:'))
        my_list = [num, num, num, num, num, num, num, num, num, num, num]
        my_list.append(num)
    print(my_list)
    return (number)
number()

