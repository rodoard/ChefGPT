# main.py

from openai import OpenAI
from utils import import_chefs

# Import all chefs dynamically
chefs = import_chefs()
      
print("\n\nWelcome to ChefGPT\n\nYour AI assistant to all things\ncooking and food preparation\n")
print("\t 1. Pass a list of ingredients to know the dish name\n")
print("\t 2. Pass a dish name to get the recipe.\n")
print("\t 3.Pass a recipe to get feedback on how to make it better.\n")
print("\n")

while True:
    print("\nYou can enter:\n\t      1. List of ingredients\n\t      2. Dish name\n\t      3. Recipe for a dish.\n")
    user_input = input()
    
    for chef in chefs:
      print(f"\n---\nGenerating chat completion with {chef.getName()}:\n")
      category = chef.getCategory(user_input)
      chef.handleInputCategory(category, user_input)
      print("\n")

