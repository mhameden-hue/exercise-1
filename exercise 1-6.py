cents = int(input("(1-100):\n"))
coins = [50, 20, 10, 5, 2, 1]
for coin in coins:
    count = cents // coin
    cents = cents % coin
    print(f"Amount of {coin} cents: {count}")