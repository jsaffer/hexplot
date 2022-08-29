from src import Pixel

import numpy as np
import matplotlib.pyplot as plt


allpixels_x = [[i for i in range(10)] for j in range(10)]
allpixels_y = [[j for i in range(10)] for j in range(10)]

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

padding1_x = [-1.0+i for i in range(12)] + 10*[-1.0, 10.0] + [-1.0+i for i in range(12)]
padding1_y = [-1.0 for i in range(12)] + [0.0, 0.0] + [1.0, 1.0] + [2.0, 2.0] + [3.0, 3.0] + [4.0, 4.0] + [5.0, 5.0] + [6.0, 6.0] + [7.0, 7.0] + [8.0, 8.0] + [9.0, 9.0] + [10.0 for i in range(12)]

padding2_x = [-2.0+i for i in range(14)] + 12*[-2.0, 11.0] + [-2.0+i for i in range(14)]
padding2_y = [-2.0 for i in range(14)] + [-1.0, -1.0] + [0.0, 0.0] + [1.0, 1.0] + [2.0, 2.0] + [3.0, 3.0] + [4.0, 4.0] + [5.0, 5.0] + [6.0, 6.0] + [7.0, 7.0] + [8.0, 8.0] + [9.0, 9.0] + [10.0, 10.0] + [11.0 for i in range(14)]

padd = 2

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
    Plot the hexagons of the IceTop grid converted to cartesian pixels, if desired together with the padding in the corners. Choose whether to fill and to immediately show the filter
    """
    if padding:
        pixpad = Pixel(ax, midpoints=[icetop_padding_x, icetop_padding_y], size=0.5, color='k')
        pixpad.draw()

    pix = Pixel(ax, midpoints=[icetop_x, icetop_y], size=0.5, color='k')
    pix.draw()
    if fill:
        corners = pix.getCorners()
        for he in corners:
            plt.fill([coords[0] for coords in he], [coords[1] for coords in he], color='k', alpha=0.15)
    if show:
        pix.show()


def plot_kernel(ax, midx, midy, kernelsize: int, fill=False, show=True):
    """
    Plot on a provided pyplot-axis object a hexagonal kernel transformed to cartesian pixels around a given mid point. Choose whether to fill and to immediately show the filter
    """
    if not isinstance(kernelsize, int) or kernelsize < 1 or kernelsize > 7: #only consider kernels up to size 7
        raise ValueError('Sorry, this kernel size is not supported!')
    if kernelsize >= 1:
        x = [midx]
        y = [midy]
    if kernelsize >= 2:
        x += [midx, midx+1.0]
        y += [midy-1.0, midy-1.0]
    if kernelsize >= 3:
        x += [midx-1.0, midx-1.0, midx, midx+1.0]
        y += [midy, midy+1.0, midy+1.0, midy]
    if kernelsize >= 4:
        x += [midx-1.0, midx, midx+1.0, midx+2.0, midx+2.0]
        y += [midy-1.0, midy-2.0, midy-2.0, midy-2.0, midy-1.0]
    if kernelsize >= 5:
        x += [midx-2.0, midx-2.0, midx-2.0, midx-1.0, midx, midx+1.0, midx+2.0]
        y += [midy, midy+1.0, midy+2.0, midy+2.0, midy+2.0, midy+1.0, midy]
    if kernelsize >= 6:
        x += [midx-2.0, midx-1.0, midx, midx+1.0, midx+2.0, midx+3.0, midx+3.0, midx+3.0]
        y += [midy-1.0, midy-2.0, midy-3.0, midy-3.0, midy-3.0, midy-3.0, midy-2.0, midy-1.0]
    if kernelsize == 7:
        x += [midx-3.0, midx-3.0, midx-3.0, midx-3.0, midx-2.0, midx-1.0, midx, midx+1.0, midx+2.0, midx+3.0]
        y += [midy, midy+1.0, midy+2.0, midy+3.0, midy+3.0, midy+3.0, midy+3.0, midy+2.0, midy+1.0, midy]
    
    pix = Pixel(ax, midpoints=[x, y], size=0.5, color='C3')
    pix.draw()
    plt.scatter(midx, midy, color='C3', marker='s')
    if fill:
        corners = pix.getCorners()
        for pi in corners:
            plt.fill([coords[0] for coords in pi], [coords[1] for coords in pi], color='C3', alpha=0.25)
    if show:
        pix.show()





make_gif_images = False
if make_gif_images:
    for i in range(len(allpixels_x)):
        fig = plt.figure(figsize=(14,9), dpi=300)
        ax = plt.subplot()

        pixpad = Pixel(ax, midpoints=[padding_x, padding_y], size=0.5, color=(0.8, 0.8, 0.8))
        pixpad.draw()
        plot_kernel(ax, allpixels_x[i], allpixels_y[i], 5, fill=True, show=False)
        plot_icetop(ax, fill=True, padding=True, show=False)

        pixpad.show(save=True, figfilename=f'icetop_hexaplot_kernel_pixel_images/icetop_hexaplot_kernel_pixel_{i+1}.png')
else:
    kernel_index = 29
    fig = plt.figure(figsize=(14,9), dpi=300)
    ax = plt.subplot()

    pixpad = Pixel(ax, midpoints=[padding_x, padding_y], size=0.5, color=(0.8, 0.8, 0.8))
    pixpad.draw()
    plot_kernel(ax, icetop_x[kernel_index-1], icetop_y[kernel_index-1], kernelsize=7, fill=True, show=False)
    plot_icetop(ax, fill=True, padding=True, show=False)

    pixpad.show(save=False)