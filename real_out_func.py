from adresses import *


def real_out(posa):
    with open(real_out_file, 'a') as f:
        tmp = str(str(posa) + '\n')
        f.write(tmp)
