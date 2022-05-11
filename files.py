"""
#1problem
a = ('csdojo', 'hackathon', 'snap', 'Документы', 'Изображения', 'Общедоступные',
'Шаблоны','github', 'itc', 'Видео', 'Загрузки', 'Музыка', 'Рабочий стол')

with open('directories.txt', 'w') as b:
	for i in a:
		b.write(i)
		b.write('\n')
	print('готово')

#2problem
login = input('введите логин: ')
password = input('введите пароль: ')

with open('users.txt', 'w') as b:
	b.write(f'{login} : {password}')
	print('готово')


#3problem
with open('users.txt', 'r') as b:
	if 'w' in b.read():
		print('Да, в тексте есть w')
	else:
		print('Нет, в тексте нет w')

#4problem

a = ('''Python is a widely used high-level programming language for general-purpose
programming, created by Guido van Rossum and first released in 1991. An interpreted
language, Python has a design philosophy that emphasizes code readability (notably
using whitespace indentation to delimit code blocks rather than curly brackets or
keywords), and a syntax that allows programmers to express concepts in fewer lines of
code than might be used in languages such as C++ or Java.''')

with open('python.txt', 'w') as b:
	b.write(f'{a}')
	print("готово")


t_words = []
with open('python.txt', 'r') as b:
	for i in b.read().split():
		if 't' in i or "T" in i:
			t_words.append(i)
print(t_words)

"""
#5problem
with open('database.txt', 'w') as a:
	a.write('merey : 123456, leva : 654321, timosha : 135642')

print('зарегистрируйтесь или войдите')

login = input('введите логин: ')
password = input('введите пароль: ')
z = input('подтвердите пароль: ')
x = input('войдите или зарегистрируйтесь: ')
with open('database.txt', 'r') as a:
	if login in a.read().split():
		print('Логин уже существует')
		print(input('авторизуйтесь используя пароль: '))
	elif a.read().split() != login:
		print('продолжите регистрацию')

	print(password)
	print(z)
	if password == z:
		with open('database.txt', 'a') as p:
			p.append(z)


