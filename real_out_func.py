from adresses import *


def real_out(posa):
    with open(real_out_file, 'w') as f:
        tmp = str(str(posa) + '\n')
        f.write(tmp)
