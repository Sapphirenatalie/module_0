# Задача «Длина слова».
# Запишите в переменную a произвольную строку.
# Затем вычислите длину строки и выведите результат на экран(в консоль).
# * для решения вам может пригодиться функция len(),
# которая позволяет определить длину строки.     

print('«Длина слова»')

a = 'странники'
length_a = len(a)

print(length_a)
print('-------------')

# Задача «Суммы и разности».
# Запишите два целых числа в переменные first и second,
# вычислите их сумму и разность, запишите их в переменные summa и diff.
# Затем выведите значения переменных summa и diff на экран(в консоль).

print('«Суммы и разности»')

first = 145
second = 97

summa = int(first) + int(second)
diff = int(first) - int(second)

print('«Сумма»: ', summa, '\n«Разность»: ', diff)
print('-------------')

# Задача «Среднее арифметическое».
# Запишите три числа в переменные first, second и third соответственно
# и вычислите их среднее арифметическое, записав в переменную mean.
# Затем выведите значения переменной mean на экран(в консоль).

print('«Среднее арифметическое»')

first = 57
second = 34
third = 83

mean = int((first + second + third) / 3)
print(mean)
print('-------------')

# Задача «Простые строчки».
# Создайте две переменных first_string и second_string
# и запишите в них строки "Вторник" и "Понедельник".
# Выведите на экран(в консоль) строки так,
# чтобы "Понедельник" шёл перед "Вторником"
# и между ними находилась запятая с пробелом (", ")
# Понедельник, Вторник

print('«Простые строчки»')

first_string = "Вторник"
second_string = "Понедельник"

print(f'{second_string}, {first_string}')
print('-------------')

# Задача «Сложная формула».
# Запишите три числа в переменные a, b и c соответственно и создайте переменную f,
# в которую запишите результат выражения: (a * b) + (a * c).
# Возведите полученное число в третью степень и результат разделите(обычное деление) на два.
# Выведите его на экран(в консоль).

print('«Сложная формула»')

a = 45
b = 22
c = 64

f = (int(a) * int(b)) + (int(a) * int(c))

f1 = (f ** 3) / 2
print(f1)
