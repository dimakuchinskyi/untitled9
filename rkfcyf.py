#ПЕРША ПАРА
'''
a = 5
b = 10
if a < b :
    print('Перше число меньше другого')
else:
    print('друге число меньше першого')


day=int(input('Введіть час в 24 годинному форматі:'))
if day<19 :
    print('Наразі день')
else:
    print('Наразі ніч')
 '''

#2 ПАРА (ЛАБОРАТОРНА)
'''
number = int(input('Введіть число:'))
if number % 2 == 0 :
    print('Even number')
else:
    print('Odd number')
'''
'''
number = int(input('Введіть число:'))
if number % 7 == 0 :
    print('Number is multiple 7')
else:
    print('Number is not multuple 7')
'''

'''
number1 = int(input('Введіть перше число:'))
number2 = int(input('Введіть друге число:'))
if number1>number2 :
    print(number1)
else:
    print(number2)
'''

'''
number1 = int(input('Введіть перше число:'))
number2 = int(input('Введіть друге число:'))
if number2<number1 :
    print(number2)
else:
    print(number1)
'''
number1 = int(input('Введіть перше число:'))
number2 = int(input('Введіть друге число:'))
print('Оберіть дію:')
print('1 - Сумма')
print('2 - Різниця')
print('3 - Середнє арефметичне')
print('4 - Добуток')

choice=input('Виберіть число з 1 до 4:')
if choice == '1':
 summa=number1+number2
 print('Сумма:' , summa)
elif choice == '2':
 riz= number1 - number2
 print('Різниця:', riz)
elif choice == '3':
 sered=(number1+number2)/2
 print('Середнє арефметичне:', sered)
elif choice == '4':
 dobutok=number1*number2
 print('Добуток:', dobutok)