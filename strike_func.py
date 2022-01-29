def get_strike(delta, strike, price):
    diff = []
    for i in strike:
        diff.append(abs(i - price))

    # d = {k:v for k, v in zip(diff, delta)}
    d = dict(zip(diff, delta))
    s = dict(zip(delta, strike))

    return d[min(d.keys())], s[d[min(d.keys())]]
