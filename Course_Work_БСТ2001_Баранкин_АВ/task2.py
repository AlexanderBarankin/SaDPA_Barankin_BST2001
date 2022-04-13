# Задание 2. Гадание на массиве

import time


def solve():

    # Ввод длины массива a, начального числа Алисы (число Боба равно x+3) и числа, которое получил один из друзей
    # в результате.

    n, x, y = map(int, input().split())
    a = list(map(int, input().split()))  # Ввод массива a

    if (sum(a) + x + y) % 2 == 0:  # Проверка массива на четность/нечетность
        print("\nAlice")  # Если четный, то число получила Алиса
    else:
        print("\nBob")  # Иначе - Боб


start_time = time.time()
for _ in range(int(input())):  # Ввод количества наборов входных данных
    solve()
print(f"{time.time() - start_time} секунд")
