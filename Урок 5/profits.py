class Company:
    def __init__(self, name, profit, duration, total):
        self.name = name
        self.profit = profit
        self.duration = duration
        self.total = total

    def sum_profit(self):
        __l = len(self.profit)
        for __ in range(__l):
            self.total += self.profit[__]
        return self.total

    def average_profit(self):
        return self.total / self.duration

companies = []
c_number = int(input('Введите число предприятий для оценки прибыли предприятий: '))
period = 4
average = 0
for __ in range(c_number):
    company_name = input(f'Введите название предприятия №{__ + 1}: ')
    company_profit = list(map(int, input(f'Введите прибыль предприятия, {period} цифры через пробел: ').split()))
    companies.append(Company(company_name, company_profit, period, 0))
    total_profit = companies[__].sum_profit()
    ap = companies[__].average_profit()
    print(f'Общая прибыль предприятия {companies[__].name} = {total_profit} ')
    print(f'Средняя прибыль предприятия {companies[__].name} за квартал = {ap}', '\n')
    average += total_profit
average = average / c_number
print(f'Средняя прибыль всех предприятий = {average}')
for __ in range(c_number):
    if companies[__].total > average:
        print(f'Предприятие {companies[__].name} имеет прибыль = {companies[__].total} - ВЫШЕ средней')
    elif companies[__].total < average:
        print(f'Предприятие {companies[__].name} имеет прибыль = {companies[__].total} - НИЖЕ средней')
    else:
        print(f'Предприятие {companies[__].name} середнячёк, прибыль = {companies[__].total} - РАВНА средней')
