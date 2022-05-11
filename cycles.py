'''
# cycles beggining
a = list(range(2, 8, 2))
print(a)

print(a[2:8:2])

for i in range(2, 8, 2):
	print(i)

###
a = [1, 3, 5, 6, 7, 8, 0, 34]
for i in a:
	print(i+2)


###

a = [1, 3, 5, 6, 8, 9, 0, 34]

for r in a:
	print(r)
	if r == 6:
		print(r)
		a.append(r)
	if len(a) > 20:
		break
print(a)


'''
'''
#problem 1
lang1 = 'Rust'
languages = ['go', 'java', 'php', 'python', 'javascript', 'ruby']
for i in languages:
	if i == lang1:
		print('this language is in list')
	else:
		print('there is no Rust')


#problem 2
languages = ['go', 'java', 'php', 'python', 'javascript', 'ruby']
for i in languages:
	print(i)
	if i == 'php':
		break

#problem 3
a = 7
for i in range(5):
	a *= 7
	print(a)


#problem 4
l = ['go', 'java', 'php', 'python', 'javascript', 'ruby']
for i in range(len(l)):
	print(i, l[i])


#problem 5
for i in range(-10,10):
	print(abs(abs(i)-10), end='')


#problem 6
for i in range(10, 21):
	for j in range(1, 11):
		print(f'{i} * {j} = {i*j}')


#problem 7
names = ('Максат', 'Лязат', 'Данияр', 'Айбек', 'Атай', 'Салават', 'Адинай', 'Жоомарт', 'Алымбек', 'Эрмек', 'Дастан', 'Бекмамат', 'Аслан')
print(names)

for i in range(len(names)):
	if i % 2 == 0:
		print(names[i])


#problem 8
names = ('Максат','Лязат','Данияр','Айбек','Атай','Салават','Адинай','Жоомарт','Алымбек','Эрмек','Дастан','Бекмамат','Аслан')
print(names)
for i in range(0,14,2):
	print(names[i])

'''


# #problem 9
# a = int(input('введите число: '))
# if a > 99 and a < 1000:
# 	print('трехзначное')
# else:
# 	print('это не трехзначное число')
# if a >= 0 and a % 2 == 0:
# 	print('положительное и четное')
# if a % 31 == 0:
# 	print('делится на 31 без остатка')
# if a > 100 and a % 17 == 0 and a > 150 and a == 13**2:
# 	print(a)


#problem 10

a = []
b = []
for i in range(-100, 100):
    if i % 13 == 0 and i % 2 == 0:
        s = i ** 2
        a.append(s)
        
    
    if i % 7 == 0 and i % 2 != 0:
        b.append(i)
        
print(a)
print(b)

