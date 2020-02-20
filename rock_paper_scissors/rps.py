#!/usr/bin/python

import sys

def helper(n, options, result):
  if n == 0:
    return result
  elif n == 1:
    return options
  else:
    return [[*x, *y] for x in options for y in helper(n - 1, options, result)]

def rock_paper_scissors(n):
  if n == 0:
    return [[]]
  result = []
  options = [["rock"], ["paper"], ["scissors"]]
  return helper(n, options, result)

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')