"""
Задача: написать функцию для сложения двух дробей, заданных числителями и знаменателями.

Результат работы функции (x, y) должен удовлетворять свойствам:
1. a/b + c/d = x/y
2. x/y несократима
3. y >= 0

Можно считать, что передаваемые в функцию b и d всегда ненулевые.
"""
def nok(n, m):
    if n > m:
        rez = n
    else:
        rez = m
    while(True):
        if rez % n == 0 and rez % m == 0:
            return rez
        else:
            rez += 1

def delitely(znam, chisl):
    s = 2
    while s <= min(abs(znam), abs(chisl)) // 2:
        while znam % s == 0 and chisl % s == 0:
            znam //= s
            chisl //= s
        s += 1
    return chisl, znam

def add_fractions(a, b, c, d):
    znam = nok(b, d)
    chisl = znam // b * a + znam // d * c
    if znam < 0:
        znam = abs(znam)
        chisl = -chisl
    print(delitely(znam, chisl))

print('Введите 4 числа')
a, b, c, d = int(input()), int(input()), int(input()), int(input())
add_fractions(a, b, c, d)



def add_fractions(a, b, c, d):
    """
    Функция сложения дробей a/b и c/d
    Должна возвращать числитель и знаменатель дроби-результата
    """
    return Ellipsis # Напишите тело функции и правильный return

