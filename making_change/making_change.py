#!/usr/bin/python

import sys

# def making_change(amount, coins, currentCoin = 0):
#   if amount == 0:
#     return 1
#   if amount < 0:
#     return 0
#   nCombos = 0
#   for coin in range(currentCoin, len(coins)):
#     nCombos += making_change(amount - coins[coin], coins, coin)
#   return nCombos

# def making_change(amount, denominations):
#   cache = {key: 0 for key in range(amount + 1)}
#   cache[0] = 1

#   for coin in denominations:
#     for val in range (coin, amount + 1):
#       cache[val] += cache[val - coin]

#   return cache[amount]

def making_change(amount, denominations):
  if amount < 0 or denominations == []:
    return 0
  if amount == 0:
    return 1
  return making_change(amount - denominations[-1], denominations) + making_change(amount, denominations[:-1])

if __name__ == "__main__":
  # Test our your implementation from the command line
  # with `python making_change.py [amount]` with different amounts
  if len(sys.argv) > 1:
    denominations = [1, 5, 10, 25, 50]
    amount = int(sys.argv[1])
    print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
  else:
    print("Usage: making_change.py [amount]")