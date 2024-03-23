# utils.py

import os
from chefFactory import newChef
def import_chefs():
    chefs = []
    chefs_dir =  os.path.join(os.path.dirname(os.path.abspath(__file__)), 'chefs')
    # Loop through files in the 'chefs' directory
    itr = 0
    for filename in os.listdir(chefs_dir):
      if filename.endswith('.py'):
        chef_name = os.path.splitext(filename)[0]  # Extract chef name from filename
        module = __import__(f'chefs.{chef_name}', fromlist=[chef_name])
        info = getattr(module, "info")
        chefs.append(newChef(info()))
    return chefs
