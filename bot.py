import time
from summ_func import *
from file_read import *
from tb import *
from write_func import *
from strike_func import *
from erase_func import *

size = 1  # pose size
pause = 60
trigger_on = 5
trigger = 0

erase()

delta_raw, strike, price = read()

delta, strike_new = get_strike(delta_raw, strike, price)
strike_old = strike_new
new_pose_size = size * delta
old_pose_size = new_pose_size
price_old = price
counter = 0

while True:
    try:
        delta_raw, strike, price = read()
    except:
        time.sleep(1)
        delta_raw, strike, price = read()

    delta, strike_new = get_strike(delta_raw, strike, price)

    # if strikes are not equal we interrupt this WHILE iteration
    if strike_new != strike_old:
        strike_old = strike_new
        new_pose_size = old_pose_size = size * delta
        print('strike change')
        f_write(summa(tmbl=True), price)
        continue

    new_pose_size = size * delta

    # if prices are the same we increase trigger by 1
    if price == price_old:
        trigger += 1
        if trigger >= trigger_on:
            send()
    else:
        trigger = 0

    if new_pose_size != old_pose_size:
        if not ((new_pose_size < 0 and old_pose_size > 0) or (new_pose_size > 0 and old_pose_size < 0)):
            if counter > 2:
                print('trend change')
                print(summa(tmbl=True), price, summa())
                f_write(summa(tmbl=True), price)
                # old_pose_size = new_pose_size
                time.sleep(5)
                # continue

        large_posa = new_pose_size - old_pose_size
        old_pose_size = new_pose_size
        posa = large_posa
        counter += 1
        f_write(posa, price)
        if counter < 2:
            print(posa, price)
        else:
            print(posa, price, summa())

    price_old = price
    time.sleep(pause)
