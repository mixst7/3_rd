"""
a = int(input("введите число: "))

if a>=0 and a<=21:
	print("разрешенное")
elif a>=57 and a<=100:
	print("разрешенное")
else:
	print("оно не разрешенно")
"""

"""
a = int(input("введите число: "))

if a % 2 == 0:
	print("четное")
else:
	print("нечетное")
if a % 3 == 0:
	print("делится на 3")
else:
	print("не делится на 3")
if a ** 2 > 1000:
	print("больше 1к")
else:
	print("меньше 1к")
"""
"""
a = int(input("введите число: "))
if a % 1 == 0 or a % 0 == 0:
	print("сработало")
else:
	print("не сработало")

"""
"""
a = 10 // 5
b = 10 / 5
Total = a + b

if a == b:
	print (a + b)
"""
"""
a = int(input("введите чило: "))
if a >= 1:
	print (-a)
"""
"""
a = 10
b = 5
if a > b:
	print (a + 2)
else:
	print (b + 2)
"""
"""
a = int(input("введите число: "))
if a > 0:
	print("положительное число")
elif a < 0:
	print("отрицательное число")
"""
"""
a = int(input("введите свой возраст: "))
if a >= 18:
	print("совершеннолетний")
elif a <= 4:
	print("ребенок")
else:
	print("несовершеннолетний")
"""
"""
a = 45
b = 6
if a % b == 0:
	print("делится")
else:
	print("не делится")
"""
"""
a = int(input("введите год: "))
if a == 2022:
	print("текущий год")
elif a < 2022:
	print("год прошел")
elif a > 2022:
	print("год еще не наступил")
"""
"""
a = int(input("введите год рождения: "))
age = 2022-a

if age >= 18:
	print("совершеннолетний")
elif age <= 4:
	print("ребенок")
elif age < 18:
	print("несовершеннолетний")
"""
"""
a = 33
b = 44
c = 55

if a > b and a > c:
	print("a")
if b > a and b > c:
	print("b")
else:
	print("c")

if a < b and a < c:
	print("a")
if b < c and b < a:
	print("b")
"""
"""
a = 17391
b = 546
c = 934
rem_1 = a % 17
rem_2 = b % 17
rem_3 = c % 17

if rem_1 < rem_2 and rem_1 < rem_3:
	print(rem_1)
elif rem_2 < rem_1 and rem_2 < rem_3:
	print(rem_2)
else:
	print(rem_3)
"""
"""
x = 13
square = x ** 2
if square >= 172:
	print(square)
elif square < 172:
	print(square ** 2)
"""

a = 26
b = 25

if a > b:
	print(a)
else:
	print(b)


