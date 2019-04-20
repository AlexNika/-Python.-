# ### --- Урок 3. Задание №4 --- ###
# ### ------- ВАРИАНТ №2 ------- ###
# ### -------------------------- ###
#
from random import randint
random_list = [randint(1, 25) for i in range(randint(1, 25))]
print(f'Массив случайных целых чисел: {random_list}')
# mrn -> most repeated number, fmax_mnr -> количество раз, которое встречается mrn
mrn = random_list[0]
fmax_mrn = 0
random_set = set(random_list)
for i in random_set:
    f = random_list.count(i)
    if f > fmax_mrn:
        fmax_mrn = f
        mrn = i
if fmax_mrn > 1:
    print(f'Число {mrn} встречается чаще всего. Оно встречается {fmax_mrn} раз')
else:
    print(f'Все элементы массива уникальны!')
