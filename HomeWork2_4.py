# ### --- Урок 2. Задание №4 --- ###
# ### -------------------------- ###
#
n = int(input('Введите количество элементов ряда (n): '))
a = 1
s = 0
for i in range(n):
    s += a
    a = a / -2
 
print(f'Сумма ряда 1 -0.5 0.25 -0.125 ... из {n} элементов = {s}')
