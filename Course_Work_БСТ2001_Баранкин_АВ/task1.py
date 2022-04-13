# Задание 1. ОКЕЯ

import time


def solve():
    n, k = map(int, input().split())  # Ввод количества и длины полок

    if k == 1:  # Если k = 1, то можно разместить товары на полках в любом порядке. Поэтому вывод "YES"
        print("\nYES")
        for i in range(1, n + 1):  # Вывод цен товаров
            print(i)
        return

    # Если количество полок нечётно, то мы не можем корректно разместить товары, так как количество чётных и нечётных
    # товаров будет отличаться как минимум на k, что невозможно. Поэтому выводим "NO"

    if n % 2 == 1:
        print("\nNO")
        return

    # В ином случае выводим "YES"

    print("\nYES")
    for i in range(1, n + 1):
        print(*[i for i in range(i, n * k + 1, n)])  # Вывод цен товаров


start_time = time.time()
for _ in range(int(input())):  # Ввод количества наборов входных данных
    solve()
print(f"{time.time() - start_time} секунд")
