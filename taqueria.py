prices = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
total_sum = 0
try:
    while True:
        input_prices = input("Item: ").title()
        if input_prices in prices:
            total = float(prices[input_prices])
            total_sum += total
            print(f"Total: ${total_sum:.2f}")
        else:
            break
except EOFError:
    pass



    