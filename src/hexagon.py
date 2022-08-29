import numpy as np
import matplotlib.pyplot as plt

def hex_corner(i: int, orientation: str, x, y, size):
    """
    For two available orientation modes, calculate the position of a hexagon's corners around the center point (x,y). Size is the distance from the mid point to the corners
    """
    if orientation == 'pointy': # corner at the top
        angle = (60*i-30)*np.pi/180.0
    elif orientation == 'flat': # flat at the top
        angle = 60*i*np.pi/180.0
    else:
        raise ValueError('Invalid orientation!')
    return x+size*np.cos(angle), y+size*np.sin(angle)


class Hexagons:
    """
    Definition of hexagons based on a list of mid points, the size and orientation. Drawing function is available
    """
    def __init__(self, axis, midpoints=[0, 0], size=1, orientation='pointy', color='k'):
        self.midpointsx = midpoints[0]
        self.midpointsy = midpoints[1]
        self.size = size
        self.orientation = orientation
        self.color = color
        self.ax = axis

    def draw(self):
        for j in range(len(self.midpointsx)):
            corners = [hex_corner(i, self.orientation, self.midpointsx[j], self.midpointsy[j], self.size) for i in range(6)]
            for i in range(6):
                self.ax.plot([corners[i-1][0], corners[i][0]], [corners[i-1][1], corners[i][1]], color=self.color)

    def show(self, save=False, figfilename=''):
        self.ax.axis('equal')
        self.ax.set_xticks([])
        self.ax.set_yticks([])
        self.ax.spines.right.set_visible(False)
        self.ax.spines.bottom.set_visible(False)
        self.ax.spines.left.set_visible(False)
        self.ax.spines.top.set_visible(False)
        if save:
            plt.savefig(figfilename, dpi=300)
            plt.close()
        else:
            plt.show()

    def getCorners(self):
        all_corners = []
        for j in range(len(self.midpointsx)):
            corners = [hex_corner(i, self.orientation, self.midpointsx[j], self.midpointsy[j], self.size) for i in range(6)]
            all_corners.append(corners)
        return all_corners



def pix_corner(i: int, x, y, size):
    """
    For two available orientation modes, calculate the position of a hexagon's corners around the center point (x,y). Size is the distance from the mid point to the corners
    """
    all_corners_x = [x+size, x+size, x-size, x-size]
    all_corners_y = [y+size, y-size, y-size, y+size]
    return all_corners_x[i], all_corners_y[i]

class Pixel:
    """
    Definition of pixels based on a list of mid points and the size. Drawing function is available.
    """
    def __init__(self, axis, midpoints=[0, 0], size=1, color='k'):
        self.midpointsx = midpoints[0]
        self.midpointsy = midpoints[1]
        self.size = size
        self.color = color
        self.ax = axis

    def draw(self):
        for j in range(len(self.midpointsx)):
            corners = [pix_corner(i, self.midpointsx[j], self.midpointsy[j], self.size) for i in range(4)]
            for i in range(4):
                self.ax.plot([corners[i-1][0], corners[i][0]], [corners[i-1][1], corners[i][1]], color=self.color)

    def show(self, save=False, figfilename=''):
        self.ax.axis('equal')
        self.ax.set_xticks([])
        self.ax.set_yticks([])
        self.ax.spines.right.set_visible(False)
        self.ax.spines.bottom.set_visible(False)
        self.ax.spines.left.set_visible(False)
        self.ax.spines.top.set_visible(False)
        if save:
            plt.savefig(figfilename, dpi=300)
            plt.close()
        else:
            plt.show()

    def getCorners(self):
        all_corners = []
        for j in range(len(self.midpointsx)):
            corners = [pix_corner(i, self.midpointsx[j], self.midpointsy[j], self.size) for i in range(4)]
            all_corners.append(corners)
        return all_corners
