import time
from summ_func import *
from file_read import *
from tb import  *
from write_func import *
from strike_func import *
from erase_func import *

size = -1  # размер позиции
pause = 5
trigger_on = 25
trigger = 0

# erase()

delta, strike, price = read()

d = get_strike(delta, strike, price)

new = size * d
old = new
price_old = price
trigger = 0
counter = 0

while True: