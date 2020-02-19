#!/usr/bin/python

import math

def recipe_batches(recipe, store_cupboard):
  whole_batches = 0
  while True:
    for ingredient in list(recipe.keys()):
      if ingredient in store_cupboard and store_cupboard[ingredient] >= recipe[ingredient]:
        store_cupboard[ingredient] -= recipe[ingredient]
      else:
        return whole_batches
    whole_batches += 1
  return whole_batches

if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))