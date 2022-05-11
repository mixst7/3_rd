# a = 'dsafkjdasngnsd'

# def func(abc):
#     s = 0
#     for i in abc:
#         s += 1
#     return s

# print(func(a))


# #1 problem

# list_1 = ['name', 'age', '1', '19']

# def func(a):
#     mid = len(a) // 2
#     b = a[:mid:]
#     c = a[mid:]
#     d = list(reversed(b)) + list(reversed(c))
#     return d


# print(func(list_1))

# #2 problem
# def fib(n):
#     a = 0
#     b = 1
#     if n == 1:
#         print(a)
#     else:
#         print(a)
#         print(b)
#         for i in range(10, n):
#             c = a + b
#             a = b
#             b = c
#             print(c)

# fib(10)


# #3 problem
# word = 'Hello World'
# def vowels(a):
#     s = 0
#     for i in a:
#         letter = i.lower()
#         if letter == 'a' or letter == 'o' or letter == 'u' or letter == 'e' or letter == 'i' or letter == 'y':
#             s += 1
#             return(s)

# print(vowels(word))        


word = 'Hello AAAA'
def count(a):
    vowels = 0
    consonants = 0
    for i in a:
        if i.isalpha():
            if i.lower() in 'aeiouy':
                vowels += 1
            else:
                consonants += 1
 
    return (vowels, consonants)

print(count(word))

# word = 'Hello World'
# def countVowels(string):
#     vowels = ['a','e','i','o','u']
#     total = 0.
#     for s in string:
#         if s in vowels:
#             total += 1

#     return total 

# print(countVowels(word))