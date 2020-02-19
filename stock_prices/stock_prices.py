#!/usr/bin/python

import argparse

def find_max_profit(prices):
  # Create a list of profits
  profits = []
  for i in range(len(prices)):
    # Take each buy price in turn
    buy_price = prices[i]
    # Create a list of potential sale prices
    sell_prices = prices[i + 1:]
    # Work out the profit for each potential sale price
    for sell_price in sell_prices:
      # And add it to the profits list
      profits.append(sell_price - buy_price)
  # Then return the maximum value from the profits list
  return max(profits)

if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))