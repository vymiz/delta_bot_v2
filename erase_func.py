from adresses import *

def erase():
    tmp = input('Erase data? ')
    if tmp == 'y':
        tmp_f = open(out, 'w')
        tmp_f.close()