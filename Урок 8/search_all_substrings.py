import hashlib
import timeit


def search_substring1(string):
    subs_set = set()
    for i in range(len(string)):
        for j in range(len(string) - 1 if i == 0 else len(string), i, -1):
            # print(string[i:j], hash(string[i:j]))
            subs_set.add(hash(string[i:j]))
    return subs_set


def search_substring2(string):
    subs_set = set()
    for i in range(len(string)):
        for j in range(len(string) - 1 if i == 0 else len(string), i, -1):
            # print(string[i:j], hashlib.sha1(string[i:j].encode('utf-8')).hexdigest())
            subs_set.add(hashlib.sha1(string[i:j].encode('utf-8')).hexdigest())
    return subs_set


my_string1 = 'Hello world!'
my_string2 = 'Beware the Jabberwock, my son! \
              The jaws that bite, the claws that catch! \
              Beware the Jubjub bird, and shun \
              The frumious Bandersnatch!'
my_subs_set1 = search_substring1(my_string1)
print(f'Количество различных подстрок в введенной КОРОТКОЙ строке (подсчет hash()): {len(my_subs_set1)}')
print(timeit.timeit('search_substring1(my_string1)',
                    setup='from __main__ import search_substring1, my_string1', number=1000))
my_subs_set2 = search_substring2(my_string1)
print(f'Количество различных подстрок в введенной КОРОТКОЙ строке (подсчет sha1()): {len(my_subs_set2)}')
print(timeit.timeit('search_substring2(my_string1)',
                    setup='from __main__ import search_substring2, my_string1', number=1000))

my_subs_set1 = search_substring1(my_string2)
print(f'Количество различных подстрок в введенной ДЛИННОЙ строке (подсчет hash()): {len(my_subs_set1)}')
print(timeit.timeit('search_substring1(my_string2)',
                    setup='from __main__ import search_substring1, my_string2', number=1000))
my_subs_set2 = search_substring2(my_string2)
print(f'Количество различных подстрок в введенной ДЛИННОЙ строке (подсчет sha1()): {len(my_subs_set2)}')
print(timeit.timeit('search_substring2(my_string2)',
                    setup='from __main__ import search_substring2, my_string2', number=1000))


# Выводы:
#   1. С помощью hash функций hash() и sha1() можно найти все подстроки заданной строки
#   2. Встроенная функция hash() предпочтительнее, т.к. она оперирует только цифрами, значит результаты
#      занимают меньшее количество памяти. А также при одинаковых при КОРОТКОЙ строке условиях встроенная
#      функция работает почти в 5 раз быстрее. При длинной строке вычисления hash и sha1 еще увеличиваются и разница
#      в скорости достигает увеличивается более чем в 6 раз.
#
#   Это объясняется сложносью вычисления хеша по алгоритму sha1, а также величиной вычисяемого хеша.
#

