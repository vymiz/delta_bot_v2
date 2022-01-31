from adresses import *

def summa():
    file = open(out, 'r')
    f = file.readlines()
    file.close()

    posa = []
    price = []
    total = []

    for i in f:
        i = i.strip().split(',')
        posa.append(int(i[0]))
        price.append(int(i[1]))

    #  here we add the las trade to close opened positions
    posa.append(-sum(posa))
    price.append(price[-1])

    for i in range(len(posa)):
        total.append(posa[i] * price[i])

    return -sum(total)