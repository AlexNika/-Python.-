# ### --- Урок 2. Задание №7 --- ###
# ### -------------------------- ###
# --- Напишите программу, доказывающую или проверяющую,
# --- что для множества натуральных чисел выполняется равенство:
# --- 1+2+...+n = n(n+1)/2, где n - любое натуральное число.

from memory_profiler import profile
from pympler import asizeof
import sys


@profile(precision=4)
def compare(n):
    solution1 = n * (n + 1) // 2
    solution2 = 0
    print(f'Размер памяти solution2 до алгоритма: {asizeof.asizeof(solution2)}')
    for i in range(1, n + 1):
        solution2 += i

    print(f'n*(n + 1)/2 = {solution1}')
    print(f'1+2+...+n = {solution2}')
    print(f'Таким образом - n*(n + 1)/2 = 1+2+...+n | {solution1 == solution2}')
    print('-------------------------------------')
    print(f'Размер памяти solution1: {asizeof.asizeof(solution1)}')
    print(f'Количество ссылок на solution1: {sys.getrefcount(solution1)}')
    print(f'Размер памяти solution2 после алгоритма: {asizeof.asizeof(solution2)}')
    print(f'Количество ссылок на solution2: {sys.getrefcount(solution2)}')


a = int(input('Input n = 100000 - the max number of natural number: '))
compare(a)
print(f'Количество ссылок на a: {sys.getrefcount(a)}')

# Комментарий А.Николаев
# Под интерпретацию программы сразу выделяется большое количество памяти - 14.7461 мегабайт.
# Это видно с помощью использования модуля profile из библиотеки memory_profiler
# Но что важно, так это то, что выделенаня память не увеличивается.
# Значит программа не превышает размер выделенной памяти под сам интерпретатор python.
#
# В тоже время, если углубиться в код, то мы можем посмотеть на 2 основных переменных
# и выледяемую под них память (на примере n=100000:
# - переменная solution1 занимает 24 байта сразу, т.к. над ней производится только одна операция
# - переменная solution2 занимает в начале 16 байта.
# - переменная solution2 занимает 24 байта после выполнения над ней оперций.
#
# Количество ссылок на solution1 и solution2 одинаково = 3.
#