# ### --- Урок 3. Задание №1 --- ###
# ### -------------------------- ###
#
d1 = tuple(range(2,100))
d2 = [0 for i in range(9)]
for i in d1:
    for j in range(2, 10):
        if i % j == 0:
            d2[j - 2] += 1
for i in range(len(d2) - 1):
    print(f'Числу {i+2} в диапазоне от 2 до 99 кратно - {d2[i]} чисел')
