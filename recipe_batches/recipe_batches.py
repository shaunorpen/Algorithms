#!/usr/bin/python

import math

def recipe_batches(recipe, store_cupboard):
  # Create a variable to store the number of whole batches
  whole_batches = 0
  while True:
    # For each ingredient the recipe requires
    for ingredient in list(recipe.keys()):
      # Check it's in the store cupboard and that we have enough of it
      if ingredient in store_cupboard and store_cupboard[ingredient] >= recipe[ingredient]:
        # And if we do, take it out the store cupboard
        store_cupboard[ingredient] -= recipe[ingredient]
      else:
        # Until we find something we don't have or don't have enough of
        return whole_batches
    # Update whole batches by one and loop again
    whole_batches += 1

if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))