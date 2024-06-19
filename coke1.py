price = int(50)
value_coin = [25, 10, 5]

while True:
    print('Amount Due:', price)
    coins = int(input('Insert Coin: ').strip())
    for num in value_coin:
        if coins == num:
            price -= coins
    if price <= 0:
        print('Change Owed:', -price)
        break