def get_strike(d, price):
    # d, price = f_read()
    d2 = {}
    l = []

    # создаем словарь, где разница ЦЕНА-СТРАЙК является ключом, а значением страйк
    for i in d.keys():
        d2[str(abs(int(price) - int(i)))] = i

    # создаем лист, состоящий из значений разницы СТРАЙК-ЦЕНА
    for i in d2.keys():
        l.append(int(i))

    # возвращаем текущий страйк, расчитанный, а не полученный
    return d2[str(min(l))]