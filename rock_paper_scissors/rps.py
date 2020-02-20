#!/usr/bin/python

import sys

def helper(n, options, result):
  # Base case: n = 0 returns empty array (from function input)
  if n == 0:
    return result
  # 2nd base case: n = 1 returns the list of options (from function input)
  elif n == 1:
    return options
  # If neither base case applies, generate a new set of results
  # using a recursive call to the helper function passing on the
  # options and results from previous call and n - 1. This is O(n^2)
  # so is a good candidate for a second pass solution, but it works
  # so I'm leaving it here for now. 
  else:
    return [[*x, *y] for x in options for y in helper(n - 1, options, result)]

def rock_paper_scissors(n):
  # If n = 0, return an array containing an empty array
  if n == 0:
    return [[]]
  # Else, recursively generate the result set using an empty array
  # and array of options as input
  result = []
  options = [["rock"], ["paper"], ["scissors"]]
  return helper(n, options, result)

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')