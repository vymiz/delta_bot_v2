file = open('../data/xxx.txt', 'r')
f = file.readlines()
file.close()

posa = []
price = []
total = []

for i in f:
    i = i.strip().split(',')
    posa.append(int(i[0]))
    price.append(int(i[1]))

for i in range(len(posa)):
    total.append(sum(posa[:i]))

print(min(total))
print((max(total)))
