from adresses import *


def f_write(posa, price):
    with open(out, 'a') as f:
        tmp = str(str(posa) + ',' + str(price) + '\n')
        f.write(tmp)
