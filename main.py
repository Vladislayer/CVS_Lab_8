from collections import OrderedDict
from collections import Counter
from functools import reduce

while True:
    cmd = input("Выберите интересующий вас пункт задания: ")
#ddfsdf
    if cmd == "1":
        def ret(*args):
            a = list()
            for i, x in enumerate(args): # i - индекс итерации цикла; x - индекс элемента в args
                a.append(x)              # добавляем элемент в лист
            return list(a)
        print(ret(1, 3, 3, 7, 'донецк'))

    if cmd == "2":
        def sortr(lst):
            lst.sort(reverse=True)
            return lst
        print(sortr([1917, 1922, 1941, 1945, 1953, 1976, 1979, 1991, 2003, 2022, 2030]))

    if cmd == "3":
        dct = OrderedDict()
        print('Введите 5 значений словаря')
        for i in range(5):
            value = input(f'Введите {i+1}-й элемент словаря: ')
            dct[i+1] = value
        print(dct)
        print("Id: " + str(id(dct)))

        # Меняем местами первый и последний элементы
        first = list(dct.items())[0]
        last = list(dct.items())[-1]
        dct.move_to_end(key=first[0])
        dct.move_to_end(key=last[0], last=False)

        # Удаляем второй элемент
        second = list(dct.items())[1]
        del dct[second[0]]

        # Вставляем новый элемент
        new_key = input('Введите new_key: ')
        new_value = input('Введите new_value: ')
        dct[new_key] = new_value
        print(dct)
        print("id: " + str(id(dct)))

    if cmd == "4":
        dct_1 = {'a': 845, 'b': 855, 'c': 860, 'd': 865, 'e': 870, 'f': 888}
        dct_2 = {'a': 8, 'c': 625, 'e': 710, 'f': 725, 'g': 695}

        def max_dct(*dicts):
            return dict(reduce(lambda a, b: Counter(a) | Counter(b), dicts))

        def sum_dct(*dicts):
            return dict(reduce(lambda a, b: Counter(a) + Counter(b), dicts))

        print(max_dct(dct_1, dct_2))
        print(sum_dct(dct_1, dct_2))

    if cmd == "5":
        def tpl_sort(tpl):
            for element in tpl:
                if not isinstance(element, int):
                    return tpl
            return tuple(sorted(tpl))
        print(tpl_sort((9, 1, 1, 6, 2)))
        print(tpl_sort((435, 4, 76.14, 15, 20)))

    if cmd == "6":
        def del_from_tuple(tpl, element):
            lst = list(tpl)
            if element in tpl:
                lst.remove(element)
            return tuple(lst)
        tpl = input('Введите кортеж: ').split()
        element = input('Введите элемент: ')
        print(del_from_tuple(tpl, element))