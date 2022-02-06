from adresses import *

def summa(tmbl = False):
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
    r = -sum(posa)
    posa.append(r)
    price.append(price[-1])

    if tmbl and len(posa) > 0:
        return r

    for i in range(len(posa)):
        total.append(posa[i] * price[i])

    return -sum(total)