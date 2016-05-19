total = int(input("Please enter change: "))
COINS = [("quarters", 25), ("dimes", 10), ("nickels", 5), ("pennies", 1)]
def getResultAndRemainder(coin_value):
    return (total // coin_value, total % coin_value)
for key, value in COINS:
    result = getResultAndRemainder(value)[0]
    total = getResultAndRemainder(value)[1]
    print(result, " ", key)
