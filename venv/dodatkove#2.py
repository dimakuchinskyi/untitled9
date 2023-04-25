#Dodatkove
import random
rand=random.random(1,50)
count=0
poputka=0

while poputka !=b:
    poputka = int(input('Спробуй вгадати число в проміжку з 1 до 50'))
    if poputka > b:
        print('Загадане число меньше цього числа')
    elif sproba<b:
        print('Загадане число більше вашого введеного числа')
        count+=1
    elif 50<poputka<0:
        print('Введіть число від 0 до 100')
