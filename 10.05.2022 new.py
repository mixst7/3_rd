
# #2 problem
# symbols = '!@#$%^&*(})_]+{/[?.,'

# def issymbols(d):
#     for i in d:
#         if i not in symbols:
#             return False
#     return True
# print(issymbols("!@!$@#@"))




# #1 problem 
# def func(b):   
#     if b.isalpha():
#         return 'only letters'
#     elif b.isdigit():
#         return 'only numbers'
#     elif issymbols(b):
#         return 'only symbols'
#     elif not b.isdigit() or not b.isalpha():
#         return 'numbers and letters'
#     elif b.isalpha() or b.isdigit() or issymbols(b):
#         return 'ALL'
    

# z = '!@#@!$WQEQWESDS3435134314'

# print(func(z))


def isdigit(p):
    num ='0123456789'
    for i in p:
        if i not in num:
            return False
    return True

def isalpha(y):
    let ='abcdefghijklmnopqrstuvwxyz'
    for i in y:
        if i not in let:
            return False
    return True

def issimvol(spisok):
    sim ='!@#$%^&*()_ +=-\][/.,'
    for i in spisok:
        if i not in sim:
            return False
    return True

def func(s):
    alpha = False
    digit = False
    simvol = False
 
    for i in s:
        if isdigit(i):
            digit = True
        elif isalpha(i):
            alpha = True
        elif issimvol(i):
            simvol = True
 
    if alpha and digit and simvol:
        return 'all'
    elif alpha and digit:
        return 'letters and numbers'
    elif alpha and simvol:
        return 'letters and symbols'
    elif digit and simvol:
        return 'numbers and symbols'
    elif simvol:
        return 'only symbols'
    elif alpha:
        return 'only letters'
    elif digit:
        return 'only numbers'

print(func('ksfdna293u0214213@#!%$@!#'))