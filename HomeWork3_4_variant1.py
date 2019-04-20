# ### --- Урок 3. Задание №4 --- ###
# ### ------- ВАРИАНТ №1 ------- ###
# ### -------------------------- ###
#
from random import randint
random_list = [randint(1, 25) for i in range(randint(1, 25))]
print(f'Массив случайных целых чисел: {random_list}')
# mrn -> most repeated number, fmax_mnr -> количество раз, которое встречается mrn
mrn = random_list[0]
fmax_mrn = 1
for i in range(len(random_list) - 1):
    f = 1
    for j in range(i + 1, len(random_list)):
        if random_list[i] == random_list[j]:
            f += 1
    if f > fmax_mrn:
        fmax_mrn = f
        mrn = random_list[i]
if fmax_mrn > 1:
    print(f'Число {mrn} встречается чаще всего. Оно встречается {fmax_mrn} раз')
else:
    print(f'Все элементы массива уникальны!')
