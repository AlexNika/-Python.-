# ### --- Урок 3. Задание №2 --- ###
# ### -------------------------- ###
#
from random import randint
random_list = [randint(0, 100) for i in range(randint(0, 100))]
print(f'Исходный массив случайных целых чисел: {random_list}')
print()
iEven_list = []
for i in range(len(random_list)):
    if random_list[i] % 2 == 0:
        iEven_list.append(i)
        
print(f'Массив индексов четных элементов исходного массива: {iEven_list}')
