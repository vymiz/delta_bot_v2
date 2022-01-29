import time
from summ_func import *
from file_read import *
from tb import *
from write_func import *
from strike_func import *
from erase_func import *
from math import copysign

size = -1  # pose size
pause = 5
trigger_on = 25
trigger = 0

erase()

delta, strike, price = read()

d, strike_new = get_strike(delta, strike, price)
strike_old = strike_new
new_pose_size = size * d
old_pose_size = new_pose_size
price_old = price
counter = 0

while True:
    delta, strike, price = read()
    d, strike_new = get_strike(delta, strike, price)

    '''   TODO it's need to do something with strike changes
    if strike_new != strike_old:  # if strikes are not equal we interrupt this WHILE iteration
        strike_old = strike_new
        new_pose_size = old_pose_size = 0
        continue
        '''

    new_pose_size = size * d

    if price == price_old:  # if prices are the same we increase trigger by 1
        trigger += 1
        if trigger >= trigger_on:
            send()
    else:
        trigger = 0

    if new_pose_size != old_pose_size:
        large_posa = new_pose_size - old_pose_size
        old_pose_size = new_pose_size
        posa = int(copysign(1, large_posa))
        counter += 1
        f_write(posa, price)
        if counter < 2:
            print(posa, price)
        else:
            print(posa, price, summa())

    price_old = price
    time.sleep(pause)
