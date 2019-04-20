# ### --- Урок 3. Задание №5 --- ###
# ### -------------------------- ###
#
from random import randint
while True:
    random_list = [randint(-10, 10) for i in range(randint(0, 20))]
    if len(random_list) != 0:
        print(f'Исходный массив случайных целых чисел: {random_list}')
        break
    else:
        print('Генератор создал пустой массив. Пробуем еще раз')
minus_flag = False
nmin = random_list[0]
i_nmin = 0
for i in range(len(random_list)):
    if random_list[i] < 0 and random_list[i] <= nmin:
        minus_flag = True
        nmin = random_list[i]
        i_nmin = i
if minus_flag == True:
    print(f'MIN число: {nmin}, index MIN числа в исходном массиве: {i_nmin}')
else:
    print('В массиве нет отрицательных элементов!')
