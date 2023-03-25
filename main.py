from tabulate import tabulate

from pozicijos import (judesiukai_x,
                       judesiukai_0,
                       judesiukai)
from win import win_x, win_0

lentele = [["-", "-", "-"],
           ["-", "-", "-"],
           ["-", "-", "-"]]

print(tabulate(lentele, tablefmt="fancy_grid"))

while True:
    x_move = int(input("Padekite X: "))
    for sk_x in judesiukai:
        if sk_x == x_move:
            print("Reikšmė jau yra, pasirenkame naują")
            x_move = int(input("vedam: "))
    if x_move == 7:
        for skaicius in lentele:
            del lentele[0][0]
            lentele[0].insert(0, "X")
    elif x_move == 8:
        for skaicius in lentele:
            del lentele[0][1]
            lentele[0].insert(1, "X")
    elif x_move == 9:
        for skaicius in lentele:
            del lentele[0][2]
            lentele[0].insert(2, "X")
    elif x_move == 4:
        for skaicius in lentele:
            del lentele[1][0]
            lentele[1].insert(0, "X")
    elif x_move == 5:
        for skaicius in lentele:
            del lentele[1][1]
            lentele[1].insert(1, "X")
    elif x_move == 6:
        for skaicius in lentele:
            del lentele[1][2]
            lentele[1].insert(2, "X")
    elif x_move == 1:
        for skaicius in lentele:
            del lentele[2][0]
            lentele[2].insert(0, "X")
    elif x_move == 2:
        for skaicius in lentele:
            del lentele[2][1]
            lentele[2].insert(1, "X")
    elif x_move == 3:
        for skaicius in lentele:
            del lentele[2][2]
            lentele[2].insert(2, "X")

    judesiukai_x.add(x_move)
    judesiukai.add(x_move)

    print(tabulate(lentele, tablefmt="fancy_grid"))
    win_x()

    if len(judesiukai_x) >= 5:
        print("Niekas nelaimėjo, lygiosios.")
        exit()

    _0_move = int(input("Padekite 0: "))
    for sk0 in judesiukai:
        if sk0 == _0_move:
            print("Reikšmė jau yra, pasirenkame naują")
            _0_move = int(input("vedam: "))
    if _0_move == 7:
        for skaicius in lentele:
            del lentele[0][0]
            lentele[0].insert(0, "0")
    elif _0_move == 8:
        for skaicius in lentele:
            del lentele[0][1]
            lentele[0].insert(1, "0")
    elif _0_move == 9:
        for skaicius in lentele:
            del lentele[0][2]
            lentele[0].insert(2, "0")
    elif _0_move == 4:
        for skaicius in lentele:
            del lentele[1][0]
            lentele[1].insert(0, "0")
    elif _0_move == 5:
        for skaicius in lentele:
            del lentele[1][1]
            lentele[1].insert(1, "0")
    elif _0_move == 6:
        for skaicius in lentele:
            del lentele[1][2]
            lentele[1].insert(2, "0")
    elif _0_move == 1:
        for skaicius in lentele:
            del lentele[2][0]
            lentele[2].insert(0, "0")
    elif _0_move == 2:
        for skaicius in lentele:
            del lentele[2][1]
            lentele[2].insert(1, "0")
    elif _0_move == 3:
        for skaicius in lentele:
            del lentele[2][2]
            lentele[2].insert(2, "0")
    judesiukai_0.add(_0_move)
    judesiukai.add(_0_move)

    print(tabulate(lentele, tablefmt="fancy_grid"))
    win_0()

