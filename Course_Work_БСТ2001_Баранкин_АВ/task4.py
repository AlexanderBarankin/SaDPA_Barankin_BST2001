# Задание 4. Отравленный кинжал

import time


def solve():
    n, h = map(int, input().split())  # Ввод количества атак Монокарпа и количества урона, которое необходимо нанести
    a = list(map(int, input().split()))  # Ввод номеров секунд атаки
    s = 0

    for x in sorted(y - x for x, y in zip(a, a[1:])):  # Бинарный поиск удовлетворяющего значения k
        if s + x * n > h:
            break
        s += x
        n -= 1

    print(" ")
    print(0 - (s - h) // n)


start_time = time.time()
for _ in range(int(input())):  # Ввод количества наборов входных данных
    solve()
print(f"{time.time() - start_time} секунд")
