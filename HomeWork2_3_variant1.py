# ### --- Задание №3, вариант 1 --- ###
# ### ----------------------------- ###
#
import re
direct_list = list(str(input('Введите число (а можно и не только число): ')))
reverse_list = "".join(direct_list[::-1])
print(re.sub(r'0*([1-9][0-9]*|0)',r'\1', reverse_list))
