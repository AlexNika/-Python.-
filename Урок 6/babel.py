# Вавилонцы решили построить удивительную башню —
# расширяющуюся к верху и содержащую бесконечное число этажей и комнат.
# Она устроена следующим образом — на первом этаже одна комната,
# затем идет два этажа, на каждом из которых по две комнаты,
# затем идёт три этажа, на каждом из которых по три комнаты и так далее:
#         ...
#     12  13  14
#     9   10  11
#     6   7   8
#       4   5
#       2   3
#         1
#
# Эту башню решили оборудовать лифтом --- и вот задача:
# нужно научиться по номеру комнаты определять,
# на каком этаже она находится и какая она по счету слева на этом этаже.
#
# Входные данные: В первой строчке задан номер комнаты N, 1 ≤ N ≤ 2 000 000 000.
#
# Выходные данные:  Два целых числа — номер этажа и порядковый номер слева на этаже.
#
# Пример:
# Вход: 13
# Выход: 6 2
#
# Вход: 11
# Выход: 5 3
# import timeit
from memory_profiler import profile
from pympler import asizeof


@profile
def bt1(room_number):
    level = 0
    floor = 0
    room = 0
    position = 0
    go = True
    print(f'floor = {asizeof.asizeof(floor)}, position = {asizeof.asizeof(position)}, room = {asizeof.asizeof(room)}')
    while go:
        for j in range(level):
            if go:
                floor += 1
                position = 0
                for g in range(level):
                    position += 1
                    room += 1
                    if room == room_number:
                        go = False
                        break
            else:
                break
        level += 1
    print(f'floor = {asizeof.asizeof(floor)}, position = {asizeof.asizeof(position)}, room = {asizeof.asizeof(room)}')
    return(floor, position)


#@profile
def bt2(room_number):
    rooms_block = 0
    last_room = 0
    last_floor = 0
    print(f'floor = {asizeof.asizeof(last_floor)}, position = {asizeof.asizeof(rooms_block)}, '
          f'room = {asizeof.asizeof(last_room)}')
    while room_number > last_room:
        rooms_block += 1
        last_room += rooms_block * rooms_block
        last_floor += rooms_block
    i = 0
    while last_room > room_number:
        last_room -= 1
        if i < rooms_block - 1:
            i += 1
        else:
            last_floor -= 1
            i = 0
    position = rooms_block - i
    print(f'floor = {asizeof.asizeof(last_floor)}, position = {asizeof.asizeof(rooms_block)}, '
          f'room = {asizeof.asizeof(last_room)}')
    return(last_floor, position)


#@profile
def bt3(room_number):
    level = 1
    floor = 0
    position = 0
    print(f'floor = {asizeof.asizeof(floor)}, position = {asizeof.asizeof(position)}, room = {asizeof.asizeof(level)}')
    go = True
    while go:
        last_room = int(level * (level + 1) * (2 * level + 1) / 6)
        if last_room >= room_number:
            last_floor = int(level * (level + 1) / 2)
            floor = last_floor - ((last_room - room_number) // level)
            position = level - ((last_room - room_number) % level)
            go = False
        level += 1
    print(f'floor = {asizeof.asizeof(floor)}, position = {asizeof.asizeof(position)}, room = {asizeof.asizeof(level)}')
    return(floor, position)


n = int(input('Введите номер комнаты: '))
print(f'Вавилонская башня. Алгоритм №1 - {bt1(n)}')
print(f'Вавилонская башня. Алгоритм №2 - {bt2(n)}')
print(f'Вавилонская башня. Алгоритм №3 - {bt3(n)}')

# Комментарий А.Николаев
# Используя профайлер памяти, определили, что под интерпертатор python выделяется:
# 14.8 мегабайта - для алгоритма bt1
# 14.8 мегабайта - для алгоритма bt2
# 14.8 мегабайта - для алгоритма bt3
# Эта память с лихвой перекрывает любую из функций алгоритма расчета задачи вавилонской башни.
#
# Переменные кода также практически не увеличивают занимаемую память, и остаются в рамках 16 байт.
# Только на самых больших числах этажей возможн увеличение памяти переменных до 24 байт.
