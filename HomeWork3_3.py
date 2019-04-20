# ### --- Урок 3. Задание №3 --- ###
# ### -------------------------- ###
#
from random import randint
random_list = [randint(1, 25) for i in range(randint(1, 25))]
print(f'Исходный массив случайных целых чисел: {random_list}')
nmin = random_list[0]
nmax = random_list[0]
i_nmin = 0
i_nmax = 0
for i in range(len(random_list)):
    if random_list[i] < nmin:
        nmin = random_list[i]
        i_nmin = i
    if random_list[i] > nmax:
        nmax = random_list[i]
        i_nmax = i
_ = random_list[i_nmin]
random_list[i_nmin] = random_list[i_nmax]
random_list[i_nmax] = _
print(f'Массив с min <---> max челыми числами: {random_list}')
print()
print(f'MIN число: {nmin}, index MIN числа в исходном массиве: {i_nmin}')
print(f'MAX число: {nmax}, index MAX числа в исходном массиве: {i_nmax}')
