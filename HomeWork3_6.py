# ### --- Урок 3. Задание №6 --- ###
# ### -------------------------- ###
#
from random import randint
while True:
    random_list = [randint(0, 25) for i in range(randint(0, 25))]
    l = len(random_list)
    if l != 0 or l > 4:
        print(f'Массив случайных целых чисел: {random_list}')
        break
    else:
        print('Генератор создал пустой или слишком маленький массив. Пробуем еще раз')
nmin = random_list[0]
nmax = random_list[0]
i_nmin = 0
i_nmax = 0
s = 0
for i in range(len(random_list)):
    if random_list[i] < nmin:
        nmin = random_list[i]
        i_nmin = i
    if random_list[i] > nmax:
        nmax = random_list[i]
        i_nmax = i
if i_nmin > i_nmax:
    i_nmix, i_nmax = i_nmax, i_nmin
print(i_nmin, i_nmax)
for i in range(i_nmin + 1, i_nmax - 1):
    s += random_list[i]

print(f'Сумма чисел межуд i_nmin и i_nmax = {s}')
