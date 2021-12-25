print('Задание 7.')


# 7. Написать программу, доказывающую или проверяющую, что для множества натуральных чисел выполняется равенство:
# 1+2+...+n = n(n+1)/2, где n — любое натуральное число.

n = int(input('Введите число: '))


def String(n):
    count = 0
    for i in range(1, n + 1):
        count += i
    return count


string = String(n)


def Equation(n):
    return n * (n + 1) / 2


equation = Equation(n)
print(f'Результат работы ряда: {string}')
print(f'Результат работы функции: {equation}')


def Comparing(string, equation):
    if string == equation:
        return 'Результаты функций одинаковы'
    else:
        return 'Результаты функций различны'


comparing = Comparing(string, equation)
print(comparing)