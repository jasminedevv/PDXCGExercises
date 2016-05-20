total = int(input("Please enter change: "))
COINS = [("quarters", 25), ("dimes", 10), ("nickels", 5), ("pennies", 1)]
for coin_name, coin_value in COINS:
    result, total = (total // coin_value, total % coin_value)
    print(result, " ", coin_name)
