# Задача 1 (просто) "Арифметика":
# Напишите в начале программы однострочный комментарий: "1st program".
# Выведите на экран(в консоль) результат: возведение числа 9 в степень 0.5, после умножение на 5.
# Предполагаемый результат: 15.0

print('1st program')

print(f'\n(9 ** 0.5) * 5 = {(9 ** 0.5) * 5}')

print('------------------')

# Задача 2 (просто) "Сравнение, or, and":
# Напишите в начале программы однострочный комментарий: "2nd program".
# Убедитесь в том что 9.99 больше 9.98 и 1000 не равно 1000.1 одновременно, выведете результат на экран(в консоль)
#  Предполагаемый результат: True

print('2nd program')
print(f'\n9.99 > 9.98 and 1000 != 1000.1  =>> {9.99 > 9.98 and 1000 != 1000.1}')

print('------------------')

# Задача 3 (средне) "Сложная арифметика":
# Напишите в начале программы однострочный комментарий: "3rd program".
# Дано два целых четырёхзначных числа: 1234 и 5678.
# Выведите на экран(в консоль) сумму серединных чисел исходных данных (23 и 67).
# Предполагаемый результат: 90

print('3rd program')

a = 1234
b = 5678

a1 = (a % 1000) // 10
b1 = (b % 1000) // 10

res = a1 + b1


print(f'два целых четырёхзначных числа: {a} и {b}')
print(f'их серединные числа: ({a} % 1000 ) // 10 = {a1} и ({b} % 1000) // 10 = {b1}')
print(f'сумма их серединных чисел: {res}')

print('------------------')

# Задача 4 (сложно) "Всё, везде и сразу":
# Напишите в начале программы однострочный комментарий: "4th program".
# Дано два дробных числа: 13.42 и 42.13.
# Необходимо убедиться в том, что целая часть хотя бы одного из чисел равна дробной части другого.
# Например: 13 == 13 (13.42, 42.13) или 42 == 42 (13.42, 42.13).
# Предполагаемые результат: True

print('4th program')

c = 13.42
d = 42.13

c1 = int((c * 100) % 100)
c2 = int((c % 100) // 1)

d1 = int((d * 100) % 100)
d2 = int((d % 100) // 1)

print(f'целая часть числа {c} ->> ({c} * 100) % 100 = {c1}')
print(f'дробная часть числа {c} ->> ({c} % 100) // 1 = {c2}')
print(f'целая часть числа {d} ->> ({d} * 100) % 100 = {d1}')
print(f'дробная часть числа {d} ->> ({d} % 100) // 1 = {d2}')

print(f'{c1} == {d2} or {c2} == {d1} ->> {c1 == d2 or c2 == d1}')
