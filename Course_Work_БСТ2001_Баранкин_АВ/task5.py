# Задание 5. Бан в чате

import time


def solve():
    k, x = map(int, input().split())  # Ввод размера треугольника и допустимого количества эмоутов
    f = 0
    r = 2 * k - 1

    #  Бинарный поиск количества сообщений, которые возможно написать до бана, для соответствующих значений k и x.

    if x < k * k:
        while r - f > 1:
            m = f + (r - f) // 2

            if m <= k:
                s = m * (m + 1) // 2
            else:
                s = k * k - (2 * k - 1 - m) * (2 * k - m) // 2

            if s < x:
                f = m
            else:
                r = m

    print(" ")
    print(r)


start_time = time.time()
for _ in range(int(input())):  # Ввод количества наборов входных данных
    solve()
print(f"{time.time() - start_time} секунд")
