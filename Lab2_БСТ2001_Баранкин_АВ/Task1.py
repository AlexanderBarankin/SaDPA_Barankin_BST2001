import random
import time
import Node

# Событийная функция
def Task1():

    # Определение размерности случайного набора данных
    length = int(input("Введите количество элементов набора данных = "))

    # Генерация случайного набора данных
    array = [random.randint(-1000, 1000 + 1) for i in range(length)]

    # Вывод полученного набора данных
    print('\nПолученный набор данных')
    print(array)

    # Выбор алгоритма поиска
    startTask = True
    while startTask == True:
        chooseAlgorithm = input("\nВыберите алгоритм поиска, введя его номер"
                                "\n1. Бинарный поиск"
                                "\n2. Бинарное дерево поиска"
                                "\n3. Поиск методом Фибоначчи"
                                "\n4. Интерполяционный поиск."
                                "\n5. Стандартная функция поиска."
                                "\nВаш ответ: ")

        if chooseAlgorithm == "1":

            # Воспользуемся бинарным поиском
            print("\nБинарный поиск: ", end=' ')

            # Дальше пользователю будет предложено добавить или удалить какой-либо элемент
            answerAdd = input('\nХотите ли вы добавить элемент в исходный массив? Введите "да" или "нет". Ваш ответ:  ')
            if answerAdd == "да":
                addElement = int(input("\nВведите новый элемент = "))
                array.append(addElement)

            answerDel = input(
                '\nХотите ли вы удалить элемент из исходного массив? Введите "да" или "нет". Ваш ответ:  ')
            if answerDel == "да":
                delElement = int(input("\nВведите индекс элемента, который необходимо удалить = "))
                array.pop(delElement)

            # Сортировка случайного набора данных и его вывод
            array.sort()
            print("\nПолученный отсортированный набор данных")
            print(array)

            # Ввод элемента, который необходимо будет найти
            value = int(input("\nВведите элемент, который необходимо найти = "))

            # Найдём введённый элемент с помощью функции бинарного поиска в исходном отсортированном массиве:

            # Функция бинарного поиска
            def binarySearch(array, value):
                mid = len(array) // 2
                low = 0
                high = len(array) - 1

                while array[mid] != value and low <= high:
                    if value > array[mid]:
                        low = mid + 1
                    else:
                        high = mid - 1
                    mid = (low + high) // 2

                if low > high:
                    print("\nВведённое число отсутствует в наборе данных")
                else:
                    print("\nИндекс найденного элемента: ", mid)

            # Вызов функции бинарного поиска
            start_time = time.time()
            binarySearch(array, value)
            print(f"{time.time() - start_time} секунд")

        elif chooseAlgorithm == "2":

            # Воспользуемся поиском через бинарное дерево

            # Сортировка случайного набора данных и его вывод
            array.sort()

            # Дальше пользователю будет предложено добавить или удалить какой-либо элемент
            answerAdd = input('\nХотите ли вы добавить элемент в исходный массив? Введите "да" или "нет". Ваш ответ:  ')
            if answerAdd == "да":
                addElement = int(input("\nВведите новый элемент = "))
                array.append(addElement)

            answerDel = input(
                '\nХотите ли вы удалить элемент из исходного массив? Введите "да" или "нет". Ваш ответ:  ')
            if answerDel == "да":
                delElement = int(input("\nВведите индекс элемента, который необходимо удалить = "))
                array.pop(delElement)

            # Сортировка случайного набора данных
            array.sort()

            #Преобразование массива в бинарное дерево
            root = None
            for i in range(len(array)):
                root = Node.insert(root, array[i], i)

            print("\nПоиск через бинарное дерево: ", end=' '
                  "\n "                                      
                  "\nПолученный отсортированный набор данных "
                  "\n ")
            Node.inorder(root)

            # Ввод элемента, который необходимо будет найти
            value = int(input("\nВведите элемент, который необходимо найти = "))

            # Функция поиска элемента в бинарном дереве
            def treeSearch(root, value):
                if root is None:
                    raise ValueError()

                if value > root.data:
                    return treeSearch(root.right, value)
                elif value < root.data:
                    return treeSearch(root.left, value)
                else:
                    print(root.index)

            # Вызов функции поиска в бинарном дереве
            start_time = time.time()
            treeSearch(root, value)
            print(f"{time.time() - start_time} секунд")


        elif chooseAlgorithm == "3":
            # Реализация поиска методом Фибоначчи
            print("\nПоиск через метод Фибоначчи: ", end=' ')

            # Дальше пользователю будет предложено добавить или удалить какой-либо элемент
            answerAdd = input('\nХотите ли вы добавить элемент в исходный массив? Введите "да" или "нет". Ваш ответ:  ')
            if answerAdd == "да":
                addElement = int(input("\nВведите новый элемент = "))
                array.append(addElement)

            answerDel = input(
                '\nХотите ли вы удалить элемент из исходного массив? Введите "да" или "нет". Ваш ответ:  ')
            if answerDel == "да":
                delElement = int(input("\nВведите индекс элемента, который необходимо удалить = "))
                array.pop(delElement)

            # Сортировка случайного набора данных и его вывод
            array.sort()
            print("\nПолученный отсортированный набор данных")
            print(array)

            # Ввод элемента, который необходимо будет найти
            value = int(input("\nВведите элемент, который необходимо найти = "))

            # Функция поиска с помощью метода Фибоначчи
            def fibonacciSearch(array, value):
                # Объявим первые 3 следующие друг за другом числа Фибоначчи: a, b и c
                a = 0
                b = 1
                c = b + a

                while c < len(array):
                    a = b
                    b = c
                    c = b + a
                index = -1

                # Сравниваем и ищем необходимый элемент
                while c > 1:
                    i = min(index + a, len(array) - 1)
                    if array[i] < value:
                        c = b
                        b = a
                        a = c - b
                        index = i
                    elif array[i] > value:
                        c = a
                        b = b - a
                        a = c - b
                    else:
                        break

                if b and index < len(array) - 1 and array[index + 1] == value:
                    print("\nИндекс найденного элемента: ", index + 1)
                else:
                    print("\nВведённое число отсутствует в наборе данных")

            # Вызов функции поиска методом Фибоначчи
            start_time = time.time()
            fibonacciSearch(array, value)
            print(f"{time.time() - start_time} секунд")

        elif chooseAlgorithm == "4":
            # Реализация интерполяционного поиска
            print("\nИнтерполяционный поиск: ", end=' ')

            # Дальше пользователю будет предложено добавить или удалить какой-либо элемент
            answerAdd = input('\nХотите ли вы добавить элемент в исходный массив? Введите "да" или "нет". Ваш ответ:  ')
            if answerAdd == "да":
                addElement = int(input("\nВведите новый элемент = "))
                array.append(addElement)

            answerDel = input(
                '\nХотите ли вы удалить элемент из исходного массив? Введите "да" или "нет". Ваш ответ:  ')
            if answerDel == "да":
                delElement = int(input("\nВведите индекс элемента, который необходимо удалить = "))
                array.pop(delElement)

            # Сортировка случайного набора данных и его вывод
            array.sort()
            print("\nПолученный отсортированный набор данных")
            print(array)

            # Ввод элемента, который необходимо будет найти
            value = int(input("\nВведите элемент, который необходимо найти = "))

            # Функция интерполяционного поиска
            def interpolationSearch(array, value):
                low = 0
                high = len(array) - 1
                check = False
                while low <= high and value >= array[low] and value <= array[high]:
                    index = low + int(((float(high - low) / (array[high] - array[low])) * (value - array[low])))
                    if array[index] == value:
                        print("\nИндекс найденного элемента: ", index)
                        check = True
                    if array[index] < value:
                        low = index + 1
                    else:
                        high = index - 1
                if check == False:
                    print("\nВведённое число отсутствует в наборе данных")

            # Вызов функции интерполяционного поиска
            start_time = time.time()
            interpolationSearch(array, value)
            print(f"{time.time() - start_time} секунд")
        elif chooseAlgorithm == "5":

            # Воспользуемся встроенной функцией поиска
            print("\nВстроенный поиск: ", end=' ')

            # Дальше пользователю будет предложено добавить или удалить какой-либо элемент
            answerAdd = input('\nХотите ли вы добавить элемент в исходный массив? Введите "да" или "нет". Ваш ответ:  ')
            if answerAdd == "да":
                addElement = int(input("\nВведите новый элемент = "))
                array.append(addElement)

            answerDel = input(
                '\nХотите ли вы удалить элемент из исходного массив? Введите "да" или "нет". Ваш ответ:  ')
            if answerDel == "да":
                delElement = int(input("\nВведите индекс элемента, который необходимо удалить = "))
                array.pop(delElement)

            # Сортировка случайного набора данных и его вывод
            array.sort()
            print("\nПолученный отсортированный набор данных")
            print(array)

            # Ввод элемента, который необходимо будет найти
            value = int(input("\nВведите элемент, который необходимо найти = "))

            # Стандартная функция, использующая линейный поиск
            def standartSearch(array, value):
                flag = False
                for i in range(len(array)):
                    if array[i] == value:
                        print("\nИндекс найденного элемента: ", i)
                        flag = True

                if flag == False:
                    print("\nВведённое число отсутствует в наборе данных")


            # Найдём введённый элемент с помощью стандартной функции поиска в отсортированном массиве:
            start_time = time.time()
            standartSearch(array, value)
            print(f"{time.time() - start_time} секунд")

        else:
            print("Введён некорректный номер алгоритма")

        # Пользователь выбирает, хочет ли он повторить процедуру поиска
        startStop = input('\nВы хотите повторить процедуру поиска, использовав другой алгоритм?'
                          '\nВведите  "да" или "нет" Ваш ответ: ')
        if startStop == "нет":
            startTask = False

# Вызов событийной функции
Task1()


















