socks, socksM = map(int, input().split())  # ввод данных в одной строке
# Каждый день минус 1 носок, каждый M день 1 носок добавляется, на сколько дней хватит носков?
days = 0
# Цикл работает пока кол-во носков больше нуля
while socks > 0:
    # Сколько носков осталось, отнимаем по одному каждый день.
    socks = socks - 1
    days = days + 1         # Увеличиваем счетчик дней
    if days % socksM == 0:  # Проверка, что настал М день, т.е. надо добавлять +1 носок от мамы
        socks = socks + 1   # Увеличиваем кол-во носков на 1 (носок от мамы)
print(days)
