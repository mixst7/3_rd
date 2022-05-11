from curses.ascii import isdigit


users = {
    '+996508080876': {
        'name': 'Kiri',
        "age": 19,
        'height': 181,
        'profession': 'Python dev',
        'cash': 1000000 
    }
}

codes = [
    '500', 
    '501',
    '502', 
    '505', 
    '507',
    '550',
    '551',
    '552',
    '553',
    '554',
    '555',
    '556',
    '557',
    '559',
    '755',
    '999',
    '771',
    '772',
    '773',
    '774',
    '775',
    '776',
    '777',
    '778',
    '779',
    '220',
    '227',
]

# while True:
#     if len(phone) == 13:
#         print('ok')
#         if phone.startswith('+996'):
#             print('ok')
#             if phone.strip('+').isdigit():
#                 print('ono isdigit')
#                 if phone[4:7] in codes:
#                     print('у вас оператор кг')
#                     break
#                 else:
#                     print('у вас иностранный оператор')
#                     phone = input('Vedite phone еще раз пример(+996500123456): ')
#             else:
#                 print('ono ne isdigit')
#                 phone = input('Vedite phone еще раз пример(+996500123456): ')
#         else:
#             print('вы не в кг, введите кг номер')
#             phone = input('Vedite phone еще раз пример(+996500123456): ')
#     else:
#         print('недостаточно символов')
#         phone = input('Vedite phone еще раз пример(+996500123456): ')
phone = input('Vedite phone пример(+996500123456): ')
while len(phone) != 13:
    phone = input('Vedite phone еще раз пример, не хватает символов: ')
    while not phone.startswith('+996'):
        phone = input('Vedite phone еще раз пример, не начинается с +996: ')
        while not phone.strip('+').isdigit():
            phone = input('Vedite phone еще раз пример:')
            while not phone[4:7] in codes:
                phone = input('Vedite phone еще раз с оператором КР: ')
            else:
                print('ok')
        else:
            print('ok')
    else:
        print('ok')
else:
    print('ok')
name = input('Vedite name : ')
age = int(input('Vedite age (цифры): '))
height = int(input('Vedite рост (цифры): '))
profession = input('Vedite профессию: ')
cash = int(input('Vedite баланс (цифры)): '))


users[phone] = {}
users[phone]['name'] = name
users[phone]['age'] = age
users[phone]['height'] = height
users[phone]['profession'] = profession
users[phone]['cash'] = cash

print(users)
