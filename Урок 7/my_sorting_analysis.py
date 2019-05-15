import random
import copy
import timeit
__author__ = 'Alexander Nikolaev'


def bubblesort(nums):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                swapped = True
    return nums


def quicksort_wr(nums):
    if len(nums) <= 1:
        return nums
    else:
        q = random.choice(nums)
    l_nums = [n for n in nums if n < q]

    e_nums = [q] * nums.count(q)
    b_nums = [n for n in nums if n > q]
    return quicksort_wr(l_nums) + e_nums + quicksort_wr(b_nums)


random_list = [random.randint(-100, 100) for __ in range(0, 100)]
print(f'Сгенерированный массив случайных целых чисел: {random_list}')
qs_list = copy.deepcopy(random_list)
bs_list = copy.deepcopy(random_list)
bs_list = bubblesort(bs_list)
qs_list = quicksort_wr(qs_list)
print()
print(f'Отсортированный BUBBLE SORT массив случайных целых чисел: {bs_list}')
print(f'Отсортированный QUICK SORT (с рекурсией) массив случайных целых чисел: {qs_list}')
print()
print('Проверяем скорость работы на примере 1, 100, 1000, 10000 и 100000 выполнений')
qs_time = timeit.timeit('quicksort_wr(qs_list)', setup='from __main__ import quicksort_wr, qs_list', number=1)
bs_time = timeit.timeit('bubblesort(bs_list)', setup='from __main__ import bubblesort, bs_list', number=1)
print(f'Bubble Sort time (1 repeats): {bs_time}')
print(f'Quick Sort time (1 repeats): {qs_time}')
print()
qs_time = timeit.timeit('quicksort_wr(qs_list)', setup='from __main__ import quicksort_wr, qs_list', number=100)
bs_time = timeit.timeit('bubblesort(bs_list)', setup='from __main__ import bubblesort, bs_list', number=100)
print(f'Bubble Sort time (100 repeats): {bs_time}')
print(f'Quick Sort time (100 repeats): {qs_time}')
print()
qs_time = timeit.timeit('quicksort_wr(qs_list)', setup='from __main__ import quicksort_wr, qs_list', number=1000)
bs_time = timeit.timeit('bubblesort(bs_list)', setup='from __main__ import bubblesort, bs_list', number=1000)
print(f'Bubble Sort time (1000 repeats): {bs_time}')
print(f'Quick Sort time (1000 repeats): {qs_time}')
print()
qs_time = timeit.timeit('quicksort_wr(qs_list)', setup='from __main__ import quicksort_wr, qs_list', number=10000)
bs_time = timeit.timeit('bubblesort(bs_list)', setup='from __main__ import bubblesort, bs_list', number=10000)
print(f'Bubble Sort time (10000 repeats): {bs_time}')
print(f'Quick Sort time (10000 repeats): {qs_time}')
print()
qs_time = timeit.timeit('quicksort_wr(qs_list)', setup='from __main__ import quicksort_wr, qs_list', number=100000)
bs_time = timeit.timeit('bubblesort(bs_list)', setup='from __main__ import bubblesort, bs_list', number=100000)
print(f'Bubble Sort time (100000 repeats): {bs_time}')
print(f'Quick Sort time (100000 repeats): {qs_time}')
print()
print('Теперь вызовем функции сортировки на реально большом массиве, но повторим всего один раз')
print('Сгенерированный массив будет содержать 100000 элементов')
print('ВНИМАНИЕ!!! ВЫПОЛНЯЕТСЯ ДОЛГО')
print('-----------------------------')
random_list = [random.randint(-1000000, 1000000) for __ in range(0, 100000)]
qs_list = copy.deepcopy(random_list)
bs_list = copy.deepcopy(random_list)
bs_list = bubblesort(bs_list)
qs_list = quicksort_wr(qs_list)
bs_time = timeit.timeit('bubblesort(bs_list)', setup='from __main__ import bubblesort, bs_list', number=1)
print(f'Bubble Sort time (1 repeats): {bs_time}')
qs_time = timeit.timeit('quicksort_wr(qs_list)', setup='from __main__ import quicksort_wr, qs_list', number=1)
print(f'Quick Sort time (1 repeats): {qs_time}')

# Выводы:
# Создано 2 функции сортировки - сортировка пузырьком и быстрая сортировка
# Оказалось, что сортировка пузырьком работает на моем компьютере быстрее
# чем быстрая сортировка.
# Это обусловлено тем, как написана функция быстрой сортировки.
# Код функции быстрой сортировки содержит 2 хвостовых рекурсии
# и это плачевно сказывается на производмтельности!
# К том же, рекурсии многократно увеличивают потребляемую память
# а сам код дополнительно генерирует 2 массива, т.к. функция не изменяет
# входящий массив данных.
# Чтобы использовать алгоритм быстрой сортировки, его надо переписать
# на языке С/С++, составить алгоритм так, чтобы работа велась над входным массивом
# а также заменить рекурсии на итерации.
# В текущем же виде сам был удивлен, что функцция быстрой сортировки на поверку оказалась
# далеко не быстрой.
# ----------------------------------------
