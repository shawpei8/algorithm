class Moon:
    def __init__(self, stock, sale):
        self.stock = stock
        self.sale = sale
        self.price = sale / stock

n, d = [int(i) for i in input().split()]

stocks = [int(i) for i in input().split()]
sales = [int(i) for i in input().split()]

moons = []
for i in range(n):
    moons.append(Moon(stocks[i], sales[i]))

moons.sort(key=lambda x: x.price, reverse=True)

profits = 0
for i in range(n):
    if d >= moons[i].stock:
        profits += float(moons[i].sale)
        d -= moons[i].stock
    else:
        profits += moons[i].price * d
        break

print('%.2f' % profits)
print()