
# #problem 1
# count = 0
# lang1 = 'Rust'
# languages = ['go', 'java', 'Rust', 'python', 'javascript', 'ruby']

# while count != len(languages):
# 	print(languages[count])
# 	if languages[count] == lang1:
# 		print('language is in list')
# 		break

# 	count += 1

# #problem 2
# i = 0
# languages = ['go', 'java', 'php', 'python', 'javascript', 'ruby']

# while i != len(languages):
# 	print(languages[i])
# 	if languages[i] == 'php':
# 		break
# 	i += 1

# #problem 3
# i = 0
# a = 7

# while i < 5:
# 	i += 1
# 	a *= 7
# 	print(a)

# #problem 4

# i = 0
# languages = ['go', 'java', 'php', 'python', 'javascript', 'ruby']

# while i < len(languages):
# 	print(i, languages[i])
# 	if i > len(languages):
# 		break
# 	i += 1


# #problem 5
# i = -20
# while True:
# 	if i >= -10:
# 		print(abs(i), end=' ')
# 	else:
# 		print(i+20, end=' ')
# 	i+=1
# 	if i == 0:
# 		break




# # calc problem


# while True:
#     a = int(input('Введите число: '))
#     b = input('Введите операцию: ' )
#     c = int(input('Введите число: '))
#     if b == '+':
#         print(a + c)
#     elif b == '-':
#         print(a - c)
#     elif b == '*':
#         print(a * c)
#     elif b == '/':
#         print(a / c)
#     elif b == '**':
#         print(a ** c)
#     elif b == '%':
#         print(a % c)
#     else:
#         print('я простой калькулятор, такое не умею')
#         break


# password = input('Введите пароль: ')
# password1 = input('Введите пароль еще раз: ')

# def confirm_password(a, b):
#     if a != b:
#         return False
#     else:
#         return True

# print(confirm_password(password, password1))

def dont_give_me_five(start,end):
    return len([i for i in range(start, end+1) if not '5' in str(i)])
       


def dont_give_me_five(a,b):
    n = []
    for i in range(a,b+1):
        if not '5' in str(i):
            n.append(i)
    return len(n)


