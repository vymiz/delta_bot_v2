import time
from summ_func import *
from file_read import *
from tb import *
from write_func import *
from strike_func import *
from erase_func import *
from math import copysign

size = 1  # pose size
pause = 60
trigger_on = 3
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
    try:
        delta, strike, price = read()
    except:
        time.sleep(1)
        delta, strike, price = read()

    d, strike_new = get_strike(delta, strike, price)

    # if strikes are not equal we interrupt this WHILE iteration
    if strike_new != strike_old:
        strike_old = strike_new
        new_pose_size = old_pose_size = size * d
        print('\tstrike change\n')
        continue

    new_pose_size = size * d

    # if prices are the same we increase trigger by 1
    if price == price_old:
        trigger += 1
        if trigger >= trigger_on:
            send()
    else:
        trigger = 0

    if new_pose_size != old_pose_size:
        large_posa = new_pose_size - old_pose_size
        old_pose_size = new_pose_size
        # posa = int(copysign(1, large_posa)) #  reduce pose size to 1 with the same SIGN
        posa = large_posa
        counter += 1
        f_write(posa, price)
        if counter < 2:
            print(posa, price, d)
        else:
            print(posa, price, d, summa())

    price_old = price
    time.sleep(pause)
