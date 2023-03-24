from tabulate import tabulate

lentele = [[7, 8, 9],
           [4, 5, 6],
           [1, 2, 3]]

print(tabulate(lentele, tablefmt="fancy_grid"))

while True:
    X_move = int(input("Padekite X: "))
    if X_move == 7:
        for skaicius in lentele:
            del lentele[0][0]
            lentele[0].insert(0, "X")
            print(tabulate(lentele, tablefmt="fancy_grid"))
            break
    elif X_move == 8:
        for skaicius in lentele:
            del lentele[0][1]
            lentele[0].insert(1, "X")
            print(tabulate(lentele, tablefmt="fancy_grid"))
            break
    elif X_move == 9:
        for skaicius in lentele:
            del lentele[0][2]
            lentele[0].insert(2, "X")
            print(tabulate(lentele, tablefmt="fancy_grid"))
            break
    elif X_move == 4:
        for skaicius in lentele:
            del lentele[1][0]
            lentele[1].insert(0, "X")
            print(tabulate(lentele, tablefmt="fancy_grid"))
            break
    elif X_move == 5:
        for skaicius in lentele:
            del lentele[1][1]
            lentele[1].insert(1, "X")
            print(tabulate(lentele, tablefmt="fancy_grid"))
            break
    elif X_move == 6:
        for skaicius in lentele:
            del lentele[1][2]
            lentele[1].insert(2, "X")
            print(tabulate(lentele, tablefmt="fancy_grid"))
            break
    elif X_move == 1:
        for skaicius in lentele:
            del lentele[2][0]
            lentele[2].insert(0, "X")
            print(tabulate(lentele, tablefmt="fancy_grid"))
            break
    elif X_move == 2:
        for skaicius in lentele:
            del lentele[2][1]
            lentele[2].insert(1, "X")
            print(tabulate(lentele, tablefmt="fancy_grid"))
            break
    elif X_move == 3:
        for skaicius in lentele:
            del lentele[2][2]
            lentele[2].insert(2, "X")
            print(tabulate(lentele, tablefmt="fancy_grid"))
            break

while True:
    _0_move = int(input("Padekite 0: "))
    if _0_move == 7:
        for skaicius in lentele:
            del lentele[0][0]
            lentele[0].insert(0, "0")
            print(tabulate(lentele, tablefmt="fancy_grid"))
            break
    elif _0_move == 8:
        for skaicius in lentele:
            del lentele[0][1]
            lentele[0].insert(1, "0")
            print(tabulate(lentele, tablefmt="fancy_grid"))
            break
    elif _0_move == 9:
        for skaicius in lentele:
            del lentele[0][2]
            lentele[0].insert(2, "0")
            print(tabulate(lentele, tablefmt="fancy_grid"))
            break
    elif _0_move == 4:
        for skaicius in lentele:
            del lentele[1][0]
            lentele[1].insert(0, "0")
            print(tabulate(lentele, tablefmt="fancy_grid"))
            break
    elif _0_move == 5:
        for skaicius in lentele:
            del lentele[1][1]
            lentele[1].insert(1, "0")
            print(tabulate(lentele, tablefmt="fancy_grid"))
            break
    elif _0_move == 6:
        for skaicius in lentele:
            del lentele[1][2]
            lentele[1].insert(2, "0")
            print(tabulate(lentele, tablefmt="fancy_grid"))
            break
    elif _0_move == 1:
        for skaicius in lentele:
            del lentele[2][0]
            lentele[2].insert(0, "0")
            print(tabulate(lentele, tablefmt="fancy_grid"))
            break
    elif _0_move == 2:
        for skaicius in lentele:
            del lentele[2][1]
            lentele[2].insert(1, "0")
            print(tabulate(lentele, tablefmt="fancy_grid"))
            break
    elif _0_move == 3:
        for skaicius in lentele:
            del lentele[2][2]
            lentele[2].insert(2, "0")
            print(tabulate(lentele, tablefmt="fancy_grid"))
            break
