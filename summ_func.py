from adresses import *

def summa(tmbl = False):
    file = open(out, 'r')
    f = file.readlines()
    file.close()

    posa = []
    price = []
    total = []

    if len(f) == 0: return 0

    for i in f:
        i = i.strip().split(',')
        posa.append(int(i[0]))
        price.append(int(i[1]))

    #  here we add the las trade to close opened positions
    r = -sum(posa)  # if TMBL True, returns inverted pose size
    posa.append(r)
    price.append(price[-1])

    if tmbl and len(posa) > 0:
        return r

    for i in range(len(posa)):
        total.append(posa[i] * price[i])

    return -sum(total)


if __name__ == '__main__':
    print(summa())
