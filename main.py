from func import *
import math
#commit 1
#ЛЕНИН
while True:  # Про switch, case в курсе
    print(
        "0. Exit  "
        "\n1. Сумма квадратов в диапазоне [a,b] "
        "\n2. Максимальное X, при условии, что X! не превышает Y "
        "\n3. Таблица умножения "
        "\n4. Количество символов определенного вида в тексте "
        "\n5. Сортировка набора чисел "
        "\n6. Поворот матрицы "
        "\n7. Расстояние от [0; 0] до [X; Y] "
        "\n8. Умножение без операции умножения "
        "\n9. Из двоичной в десятичную")
    try:
        a = int(input("Changing: "))  # Выборы
    except:
        print("Otval!")
        a = 66
    if a == 0:
        break
    if a == 1:
        x = 0
        try:
            b = integerParse("b: ")
            c = integerParse("c: ")
        except:
            print("Otval!")
        for i in range(b, c + 1):
            x += i ** 2
        print(x)
        k = input("Press \"Enter\" to continue")
    if a == 2:
        s = 0
        try:
            b = integerParse("b: ")
        except:
            print("Otval!")
        for i in range(0, b):
            if fact(i) <= b:
                s = i
        print(s)
        k = input("Press \"Enter\" to continue")
    if a == 3:
        print(
            "2 * 1 = 2        3 * 1 = 3        4 * 1 = 4        5 * 1 = 5        6 * 1 = 6        7 * 1 = 7        8 * 1 = 8        9 * 1 = 9        10 * 1 = 10"
            "\n2 * 2 = 4        3 * 2 = 6        4 * 2 = 8        5 * 2 = 10       6 * 2 = 12       7 * 2 = 14       8 * 2 = 16       9 * 2 = 18       10 * 2 = 20"
            "\n2 * 3 = 6        3 * 3 = 9        4 * 3 = 12       5 * 3 = 15       6 * 3 = 18       7 * 3 = 21       8 * 3 = 24       9 * 3 = 27       10 * 3 = 30"
            "\n2 * 4 = 8        3 * 4 = 12       4 * 4 = 16       5 * 4 = 20       6 * 4 = 24       7 * 4 = 28       8 * 4 = 32       9 * 4 = 36       10 * 4 = 40"
            "\n2 * 5 = 10       3 * 5 = 15       4 * 5 = 20       5 * 5 = 25       6 * 5 = 30       7 * 5 = 35       8 * 5 = 40       9 * 5 = 45       10 * 5 = 50"
            "\n2 * 6 = 12       3 * 6 = 18       4 * 6 = 24       5 * 6 = 30       6 * 6 = 36       7 * 6 = 42       8 * 6 = 48       9 * 6 = 54       10 * 6 = 60"
            "\n2 * 7 = 14       3 * 7 = 21       4 * 7 = 28       5 * 7 = 35       6 * 7 = 42       7 * 7 = 49       8 * 7 = 56       9 * 7 = 63       10 * 7 = 70"
            "\n2 * 8 = 16       3 * 8 = 24       4 * 8 = 32       5 * 8 = 40       6 * 8 = 48       7 * 8 = 56       8 * 8 = 64       9 * 8 = 72       10 * 8 = 80"
            "\n2 * 9 = 18       3 * 9 = 27       4 * 9 = 36       5 * 9 = 45       6 * 9 = 54       7 * 9 = 63       8 * 9 = 72       9 * 9 = 81       10 * 9 = 90"
            "\n2 * 10 = 20      3 * 10 = 30      4 * 10 = 40      5 * 10 = 50      6 * 10 = 60      7 * 10 = 70      8 * 10 = 80      9 * 10 = 90      10 * 10 = 100")
        k = input("Press \"Enter\" to continue")
    if a == 4:
        b = ""
        s = 0
        while len(b) != 20:
            b = list(func(r'[a-z]', "b: "))
        try:
            c = input("c: ")
        except:
            print("Otval!")
        s = b.count(c)
        print(s)
        k = input("Press \"Enter\" to continue")
    if a == 5:
        a = 1
        s = []
        try:
            while len(s) != 10:
                b = integerParse("b: ")
                #if b >= 0 or b <= 0:
                s.append(b)
        except:
            print("Otval!")
        s.sort()
        print(s)
        k = input("Press \"Enter\" to continue")
    if a == 6:
        matrix = [[8, 2, 5, 3, 4],
                  [9, 5, 4, 1, 3],
                  [3, 1, 3, 0, 9],
                  [4, 7, 1, 9, 0],
                  [7, 3, 7, 8, 9]]
        for s in matrix:
            print(*s)
        print("")
        rot_matrix = list_rot90(matrix)
        for s in rot_matrix:
            print(*s)
        print("")
        s = input("Press \"Enter\" to continue")
    if a == 7:
        try:
            b = floatParse("b: ")  # X длина
            c = floatParse("c: ")  # Y высота
        except:
            print("Otval!")
        # Начальные координаты [0; 0]
        s = math.sqrt(b ** 2 + c ** 2)
        print(s)
        k = input("Press \"Enter\" to continue")
    if a == 8:
        s = 0
        try:
            b = integerParse("b: ")  # X длина
            c = integerParse("c: ")  # Y высота
        except:
            print("Otval!")
        for i in range(0, c):
            s += b
        print(s)
        k = input("Press \"Enter\" to continue")
    if a == 9:
        a = func(r'[0-1]', "A: ")
        try:
            a = int(a, 2)
            print(a)
        except:
            print("OTVAL!!!")
        k = input("Press \"Enter\" key to continue")
    if a == 66:
        print()
