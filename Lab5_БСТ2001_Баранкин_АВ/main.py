# Реализация треугольника Серпинского
import turtle as t
import time


#  Функция рисует треугольник по координатам трёх точек
def draw_triangle(san):
    t.penup()
    t.goto(san[0])
    t.pendown()
    t.goto(san[1])
    t.goto(san[2])
    t.goto(san[0])


# Функция производит расчёт координат средней точки, возвращая 2 точки
def get_mid(a, b):
    x = (a[0] + b[0]) / 2
    y = (a[1] + b[1]) / 2
    return [x, y]


# Функция треугольника Серпинского
def draw_san(size, i):

    # Нарисовать треугольник
    draw_triangle(size)
    if i > 0:
        # Нарисуйте маленький треугольник слева
        size2 = [size[0], get_mid(size[0], size[1]), get_mid(size[0], size[2])]
        draw_san(size2, i - 1)

        # Нарисуйте верхний треугольник
        size3 = [get_mid(size[0], size[2]), get_mid(size[1], size[2]), size[2]]
        draw_san(size3, i - 1)

        # Нарисуйте маленький треугольник справа
        size4 = [get_mid(size[0], size[1]), size[1], get_mid(size[1], size[2])]
        draw_san(size4, i - 1)


# Основная функция
def main():
    print("=== Добро пожаловать в программу реализации фрактала 'Салфетка Серпинского'! ===")

    # Количество вызовов рекурсии. Задание глубины фрактала.
    deep: int = 0
    try:
        deep = int(input("\nВведите значение глубины фрактала: "))

    except ValueError:
        print("\nОтвет некорректен. Нужно вводить число")

    start_time = time.time()
    t.speed(1000)

    # Начальные координаты треугольника
    points = [[-200, 0], [200, 0], [0, 300]]

    # Вызов функции треугольника Серпинского
    draw_san(points, deep)
    print("\nОтрисовка фрактала полностью завершена")
    print(f"\nВремя выполнения составило: {time.time() - start_time} секунд")

    t.exitonclick()
    print("\n=== Сеанс завершён. Всего доброго! ===")


main()
