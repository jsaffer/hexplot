from src import Hexagons

import numpy as np
import matplotlib.pyplot as plt


fig = plt.figure(figsize=(14,9), dpi=300)
ax = plt.subplot()

x = [1, 4, 3]
y = [1, -1, 2.5]
size = [1, 1.6, 0.8]
orientation = ['pointy', 'flat', 'pointy']
color = ['C1', 'C4', 'C8']

hex = Hexagons(ax, midpoints=[x, y], size=size, orientation=orientation, color=color)
hex.draw()
hex.show(save=True, figfilename='./some_hexagons.png')