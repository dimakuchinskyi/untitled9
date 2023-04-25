'''
a = True
b = 12
c = 4.7
d = 'hell'
print(type(a))
print(type(b))
print(type(c))
print(float(b))
print(b * 2)
'''
'''
gold = int(input('gold:'))
diamant = int(input('diamant:'))
silver = int(input('silver:'))
if diamant >= 50 and silver >= 70:
    print('2 level')
elif gold >= 40 or diamant >= 50:
    print('3 level')
else:
    print('мало')
'''


gender=input('Введіть свою стать:')
age=int(input('Введіть свій вік:')
if 0 < age <= 1 and gender =='male':
    print('немовля, дівчинка')
elif 0 < age <= 1 and gender == 'female':
    print('Немовля, хлопчик')
elif 1 < age <= 12 and gender == 'male':
    print('Дитина, хлопчик')
elif 1 < age <= 12 and gender == 'female':
    print('Дитина, дівчинка')
elif 12 < age <= 18 and gender =='male':
    print('Підліток, хлопчик')
elif 12 < age <= 18 and gender == 'female':
    print('Підліток, дівчина')

