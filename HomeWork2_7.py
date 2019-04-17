# ### --- Урок 2. Задание №7 --- ###
# ### -------------------------- ###
#
n = int(input('Введите n - максимальное число натурального ряда: '))
solution1 = n * (n + 1) // 2
solution2 = 0
for i in range(1, n + 1):
    solution2 += i
print(f'n*(n + 1)/2 = {solution1}')
print(f'1+2+...+n = {solution2}')
print(f'Таким образом - n*(n + 1)/2 = 1+2+...+n | {solution1 == solution2}')
