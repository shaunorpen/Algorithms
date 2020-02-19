#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution
def eating_cookies(n, cache=None):
  # If we get an empty cache, initialise it with zeros
  if cache == None:
    cache = [0] * (n + 1)
  # If the cache contains a value for eating_cookies(n), return it
  if cache[n] != 0:
    return cache[n]
  # Otherwise go through the base cases first, adding
  elif n == 0:
    cache[n] = 1
  elif n <= 1:
    cache[n] = 1
  elif n == 2:
    cache[2] = 2
  elif n == 3:
    cache[3] = 4
  # And only if you have to, calculate the recursive value of eating_cookies(n)
  else:
    # Add the calculated value to the cache
    cache[n] = eating_cookies(n - 1, cache) + eating_cookies(n - 2, cache) + eating_cookies(n - 3, cache)
  # Then return it from the cache
  return cache[n]

print(eating_cookies(50, [0 for i in range(51)]))

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')