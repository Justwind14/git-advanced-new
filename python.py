print("hey")

def binary_search(someList: list) -> function:
    """Функция поиска числа в массиве чисел.

    :params:
        - someList: массив чисел

    :type someList: list

    :return: Возвращает результат внутренней функции binary_search_helper
    """

    def binary_search_helper(someList: list, number: int) -> int:
        """Внутренняя функция, хранящая в себе алгоритм бинарного поиска.

        :params:
            - someList: массив чисел
            - искомое число

        :type someList: list
        :tyoe number: int

        :return: Возвращает искомое число, если он присутствует в масиве, либо -1, если такого числа в принимаемом массиве нет
        """

        # создаем переменную, хранящую в себе индекс среднего элемента массива
        delimiter = len(someList) // 2

        if someList[delimiter] > number:
            return binary_search_helper(someList[:delimiter], number)
        if someList[delimiter] < number:
            return binary_search_helper(someList[delimiter:], number)
        if someList[delimiter] == number:
            return someList[delimiter]
        else:
            return -1

    if len(someList) != 0:
        # возвращаем результат работы внутренней функции с искомым параметром number
        return lambda number: binary_search_helper(someList, number)
    else:
        # если массив пустой, вызов функции ничего не вернет
        return None
    

print('oh my God')