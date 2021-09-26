goods = [57.8, 46.51, 97, 10, 23.25, 31.20, 45.93, 53.14, 14, 8888]
for good in goods:
    rub = int(good)
    coin = (good - rub) * 100
    print(f'{rub} руб {coin:02.0f} коп', end= ', ')

goods = [57.8, 46.51, 97, 10, 23.25, 31.20, 45.93, 53.14, 14, 8888]
goods.sort()
print(id(goods))
print(id(goods))

for good in goods:
    rub = int(good)
    coin = (good - rub) * 100
    print(f'{rub} руб {coin:02.0f} коп', end=', ')

goods = [57.8, 46.51, 97, 10, 23.25, 31.20, 45.93, 53.14, 14, 8888]
for good in sorted(goods)[::]:
    rub = int(good)
    coin = (good - int(good)) * 100
    print(f'{rub} руб {coin:02.0f} коп', end=', ')

print([f'{int(good)} руб {(good - int(good)) * 100:02.0f} коп' for good in sorted(goods)[::-1][:5]])