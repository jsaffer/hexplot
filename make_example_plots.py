from src import Hexagons

import numpy as np
import matplotlib.pyplot as plt


### singel hexagons ###

fig = plt.figure(figsize=(10,7), dpi=300)
ax = plt.subplot()

x = [1, 4, 3.1]
y = [1, -1, 2.1]
size = [1.5, 2.1, 1.1]
orientation = ['pointy', 'flat', 'pointy']
color = ['C1', 'C3', 'C0']
lw = [2.2, 1.6, 0.8]
fill = [True, False, False]

hex = Hexagons(ax, midpoints=[x, y], size=size, orientation=orientation, color=color, lw=lw, fill=fill)
hex.draw()
hex.show(save=False, figfilename='./some_hexagons.png')



### hexagonal grid ###

fig = plt.figure(figsize=(10,7), dpi=300)
ax = plt.subplot()

x = []
for i in range(5):
    x.append([np.sqrt(3)*i+np.sqrt(3)/2 for i in range(10)])
    x.append([np.sqrt(3)*i for i in range(10)])
y = [[0.0 + 1.5*j for i in range(10)] for j in range(10)]
size = 100*[1]
orientation = 100*['pointy']
color = 100*['k']
lw = 100*[1]
fill = 100*[False]

hex = Hexagons(ax, midpoints=[x, y], size=size, orientation=orientation, color=color, lw=lw, fill=fill)
hex.draw()
hex.show(save=False, figfilename='./some_hexagongrid.png')