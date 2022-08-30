from src import Hexagons

import numpy as np
import matplotlib.pyplot as plt


allpixels_x = [[np.sqrt(3)*i+np.sqrt(3)/2*j for i in range(10)] for j in range(10)]
allpixels_y = [[0.0 + 1.5*j for i in range(10)] for j in range(10)]

allpixels_x = np.array([item for sublist in allpixels_x for item in sublist])
allpixels_y = np.array([item for sublist in allpixels_y for item in sublist])

icetop_mask = [0, 0, 0, 0, 1, 1, 1, 1, 1, 1,
               0, 0, 0, 1, 1, 1, 1, 1, 1, 1,
               0, 0, 1, 1, 1, 1, 1, 1, 1, 1,
               0, 1, 1, 1, 1, 1, 1, 1, 1, 1,
               1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
               1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
               1, 1, 1, 1, 1, 1, 1, 1, 1, 0,
               1, 1, 1, 1, 1, 1, 1, 1, 0, 0,
               1, 1, 1, 1, 1, 1, 1, 0, 0, 0,
               1, 1, 1, 1, 0, 0, 0, 0, 0, 0]
icetop_mask = np.array([True if item==1 else False for item in icetop_mask])
padding_mask = np.invert(icetop_mask)

icetop_x = allpixels_x[icetop_mask]
icetop_y = allpixels_y[icetop_mask]
icetop_padding_x = allpixels_x[padding_mask]
icetop_padding_y = allpixels_y[padding_mask]


padd = 2

padding1_x = [np.sqrt(3)*i-3*np.sqrt(3)/2 for i in range(12)] + [-np.sqrt(3), 10*np.sqrt(3)] + [-np.sqrt(3)/2, 21*np.sqrt(3)/2] + [0, 11*np.sqrt(3)] + [np.sqrt(3)/2, 23*np.sqrt(3)/2] + [np.sqrt(3), 12*np.sqrt(3)] + [3*np.sqrt(3)/2, 25*np.sqrt(3)/2] + [2*np.sqrt(3), 13*np.sqrt(3)] + [5*np.sqrt(3)/2, 27*np.sqrt(3)/2] + [3*np.sqrt(3), 14*np.sqrt(3)] + [7*np.sqrt(3)/2, 29*np.sqrt(3)/2] + [np.sqrt(3)*i+4*np.sqrt(3) for i in range(12)]
padding1_y = [-1.5 for i in range(12)] + [0.0, 0.0] + [1.5, 1.5] + [3.0, 3.0] + [4.5, 4.5] + [6.0, 6.0] + [7.5, 7.5] + [9.0, 9.0] + [10.5, 10.5] + [12.0, 12.0] + [13.5, 13.5] + [15.0 for i in range(12)]

padding2_x = [np.sqrt(3)*i-3*np.sqrt(3) for i in range(14)] + [-5*np.sqrt(3)/2, 21*np.sqrt(3)/2] + [-2*np.sqrt(3), 11*np.sqrt(3)] + [-3*np.sqrt(3)/2, 23*np.sqrt(3)/2] + [-1*np.sqrt(3), 12*np.sqrt(3)] + [-np.sqrt(3)/2, 25*np.sqrt(3)/2] + [0.0, 13*np.sqrt(3)] + [np.sqrt(3)/2, 27*np.sqrt(3)/2] + [np.sqrt(3), 14*np.sqrt(3)] + [3*np.sqrt(3)/2, 29*np.sqrt(3)/2] + [2*np.sqrt(3), 15*np.sqrt(3)] + [5*np.sqrt(3)/2, 31*np.sqrt(3)/2] + [3*np.sqrt(3), 16*np.sqrt(3)] + [np.sqrt(3)*i+7*np.sqrt(3)/2 for i in range(14)]
padding2_y = [-3.0 for i in range(14)] + [-1.5, -1.5] + [0.0, 0.0] + [1.5, 1.5] + [3.0, 3.0] + [4.5, 4.5] + [6.0, 6.0] + [7.5, 7.5] + [9.0, 9.0] + [10.5, 10.5] + [12.0, 12.0] + [13.5, 13.5] + [15.0, 15.0] + [16.5 for i in range(14)]

if padd == 1:
    padding_x = padding1_x
    padding_y = padding1_y
elif padd == 2:
    padding_x = padding1_x + padding2_x
    padding_y = padding1_y + padding2_y
else:
    raise ValueError('Invalid padding option!')


def plot_icetop(ax, fill=False, show=True, padding=True):
    """
    Plot the hexagons of the IceTop grid, if desired together with the padding in the corners. Choose whether to fill and to immediately show the filter
    """
    if padding:
        hexapad = Hexagons(ax, midpoints=[icetop_padding_x, icetop_padding_y], size=1, orientation='pointy', color='k')
        hexapad.draw()

    hexa = Hexagons(ax, midpoints=[icetop_x, icetop_y], size=1, orientation='pointy', color='k')
    hexa.draw()
    if fill:
        corners = hexa.getCorners()
        for he in corners:
            plt.fill([coords[0] for coords in he], [coords[1] for coords in he], color='k', alpha=0.15)
    if show:
        hexa.show()


def plot_kernel(ax, midx, midy, kernelsize: int, fill=False, show=True):
    """
    Plot on a provided pyplot-axis object a hexagonal kernel around a given mid point. Choose whether to fill and to immediately show the filter
    """
    if not isinstance(kernelsize, int) or kernelsize < 1 or kernelsize > 7: #only consider kernels up to size 7
        raise ValueError('Sorry, this kernel size is not supported!')
    if kernelsize >= 1:
        x = [midx]
        y = [midy]
    if kernelsize >= 2:
        x += [midx+np.sqrt(3)/2, midx-np.sqrt(3)/2]
        y += [midy-1.5, midy-1.5]
    if kernelsize >= 3:
        x += [midx-np.sqrt(3), midx-np.sqrt(3)/2, midx+np.sqrt(3)/2, midx+np.sqrt(3)]
        y += [midy, midy+1.5, midy+1.5, midy]
    if kernelsize >= 4:
        x += [midx+3*np.sqrt(3)/2, midx+np.sqrt(3), midx, midx-np.sqrt(3), midx-3*np.sqrt(3)/2]
        y += [midy-1.5, midy-3, midy-3, midy-3, midy-1.5]
    if kernelsize >= 5:
        x += [midx-2*np.sqrt(3), midx-3*np.sqrt(3)/2, midx-np.sqrt(3), midx, midx+np.sqrt(3), midx+3*np.sqrt(3)/2, midx+2*np.sqrt(3)]
        y += [midy, midy+1.5, midy+3, midy+3, midy+3, midy+1.5, midy]
    if kernelsize >= 6:
        x += [midx+5*np.sqrt(3)/2, midx+2*np.sqrt(3), midx+3*np.sqrt(3)/2, midx+np.sqrt(3)/2, midx-np.sqrt(3)/2, midx-3*np.sqrt(3)/2, midx-2*np.sqrt(3), midx-5*np.sqrt(3)/2]
        y += [midy-1.5, midy-3, midy-4.5, midy-4.5, midy-4.5, midy-4.5, midy-3, midy-1.5]
    if kernelsize == 7:
        x += [midx-3*np.sqrt(3), midx-5*np.sqrt(3)/2, midx-2*np.sqrt(3), midx-3*np.sqrt(3)/2, midx-np.sqrt(3)/2, midx+np.sqrt(3)/2, midx+3*np.sqrt(3)/2, midx+2*np.sqrt(3), midx+5*np.sqrt(3)/2, midx+3*np.sqrt(3)]
        y += [midy, midy+1.5, midy+3, midy+4.5, midy+4.5, midy+4.5, midy+4.5, midy+3, midy+1.5, midy]
    
    hexa = Hexagons(ax, midpoints=[x, y], size=1, orientation='pointy', color='C3')
    hexa.draw()
    plt.scatter(midx, midy, color='C3', marker='h')
    if fill:
        corners = hexa.getCorners()
        for he in corners:
            plt.fill([coords[0] for coords in he], [coords[1] for coords in he], color='C3', alpha=0.25)
    if show:
        hexa.show()





make_gif_images = False
if make_gif_images:
    for i in range(len(allpixels_x)):
        fig = plt.figure(figsize=(14,9), dpi=300)
        ax = plt.subplot()

        hexapad = Hexagons(ax, midpoints=[padding_x, padding_y], size=1, orientation='pointy', color=(0.8, 0.8, 0.8))
        hexapad.draw()
        plot_kernel(ax, allpixels_x[i], allpixels_y[i], 5, fill=True, show=False)
        plot_icetop(ax, fill=True, padding=True, show=False)
        #hexa_it = Hexagons(ax, midpoints=[icetop_x, icetop_y], size=1, orientation='pointy')
        #hexa_it.draw()

        hexapad.show(save=True, figfilename=f'icetop_hexaplot_kernel_images/icetop_hexaplot_kernel_{i+1}.png')
else:
    kernel_index = 29
    fig = plt.figure(figsize=(14,9), dpi=300)
    ax = plt.subplot()

    hexapad = Hexagons(ax, midpoints=[padding_x, padding_y], size=1, orientation='pointy', color=(0.8, 0.8, 0.8))
    hexapad.draw()
    plot_kernel(ax, icetop_x[kernel_index-1], icetop_y[kernel_index-1], 5, fill=True, show=False)
    plot_icetop(ax, fill=True, padding=True, show=False)

    hexapad.show(save=False)