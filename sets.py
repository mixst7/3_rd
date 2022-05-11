'''
#problem 1
dates_of_birth = {3,10,11,13,31,21,1,10,3,5,6,6}
dates_of_birth.remove(6)
print(dates_of_birth)

#problem 2
farm_1 = {"dog", "cat", "mouse", "sheep"}
farm_2 = {"cow", "horse", "donkey", "cat", "dog"}
print(farm_1.intersection(farm_2))

#problem 3
farm_1 = {"dog", "cat", "mouse", "sheep"}
farm_2 = {"cow", "horse", "donkey", "cat", "dog"}

print(farm_2.difference(farm_1))


#problem 4
a = {'str', True, 0, (tuple), 'like'}
a.add('time')
a.pop9()
print(a)

#problem 5
menu = {'lagman': 120, 'plov': 120, 'borsh': 100} 
menu.update({'besh_barmak': 130})
print(menu)
menu.update({'lagman':135})
print(menu)
menu.pop('borsh')
print(menu)

#problem 6
menu = {'lagman': 120, 'plov': '120', 'borsh': 100}
menu['drinks'] = 'coca-cola', 'sprite', 'fanta'
print(menu)

#problem 7
set1 = {'.add', '.remove', '.clear', 'update', 'difference', '.diskard', '.intersection', 'intersection_update', '.pop'}
set2 = {'.clear', 'get', 'keys', 'values', 'items', 'update'}

print(set1.intersection(set2))

#problem 8
a = ['Argentina', 'Bolivia', 'Brazil', 'Chile',
 'Colombia', 'Ecuador', 'Guyana', 'Paraguay', 'Peru', 
'Suriname', 'Suriname', 'Uruguay', 'Venezuela']
a.remove('Suriname')
print(a)


#problem 9
suitcase = []
things = ['shirt', 'pants', 'phone', 'brush', 'glasses']
suitcase.extend(things)
print(suitcase)

suitcase.remove('glasses')
print(suitcase)
'''
