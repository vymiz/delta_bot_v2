import openpyxl
from adresses import *

def read():
    delta = []
    strike = []
    price = 0
    excel_file = openpyxl.load_workbook(xl)
    data_sheet = excel_file['src']
    currently_active_sheet = excel_file.active

    cells = data_sheet['A1':'C10']

    for d, s, p in cells:
        # print(f'{delta.value}, {strike.value}, {price.value}')
        delta.append(int(d.value*100))
        strike.append(s.value)
        price = p.value

    return delta, strike, price

# print(read())

'''
Sub Save1()
Application.DisplayAlerts = False
ThisWorkbook.Save
Application.DisplayAlerts = True

Application.OnTime Now + TimeValue("00:01:00"), "Save1"
End Sub
'''