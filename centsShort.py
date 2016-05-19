total = int(input("Please enter change: "))
coins = [("quarters", 25), ("dimes", 10), ("nickels", 5), ("pennies", 1)]
def getResultAndRemainer(coin_value):
    return (total // coin_value, total % coin_value)
for key, value in coins:
    result = getResultAndRemainer(value)[0]
    total = getResultAndRemainer(value)[1]
    print(result, " ", key)
