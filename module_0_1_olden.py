# Практическое задание по уроку Базовые структуры данных
# Были даны числа:
# 1. 23891471923807487.142352314353455
# 2. 23891471923807487.142352314356734
# 3. 23891471923843245.142352314334563
# 4. 23891471923843245.142352314334553
# Нужно было проверить что сумма 1 и 3 числа больше суммы 2 и 4.
# Результат должен получится False (Ложь).    

a1 = 23891471923807487.142352314353455
a2 = 23891471923807487.142352314356734
a3 = 23891471923843245.142352314334563
a4 = 23891471923843245.142352314334553

b = int(a1) + int(a3)
c = int(a2) + int(a4)

print(b > c)
