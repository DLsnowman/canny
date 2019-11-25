from __future__ import division
from gaussian_filter import gaussian
from gradient import gradient
from nonmax_suppression import maximum
from numpy import array, zeros, max
from PIL import Image
from matplotlib.pyplot import imshow, show, subplot, figure, gray, title, axis

def thresholding(im):
    thres  = zeros(im.shape)
    strong = 1.0
    weak   = 0.5
    mmax = max(im)
    lo, hi = 0.1 * mmax, 0.8 * mmax
    strongs = []
    for i in range(im.shape[0]):
        for j in range(im.shape[1]):
            px = im[i][j]
            if px >= hi:
                thres[i][j] = strong
                strongs.append((i, j))
            elif px >= lo:
                thres[i][j] = weak
    return thres, strongs

if __name__ == '__main__':
    # from sys import argv
    # if len(argv) < 2:
    #     print("Usage: python %s <image>" % argv[0])
    #     exit()
    im_path = '/tfshare/PycharmProjects/canny/valve.png'
    im = array(Image.open(im_path))
    im = im[:, :, 0]
    gim = gaussian(im)
    grim, gphase = gradient(gim)
    gmax = maximum(grim, gphase)
    thres = thresholding(gmax)
    gray()

    subplot(1, 2, 1)
    imshow(im)
    axis('off')
    title('Original')

    subplot(1, 2, 2)
    imshow(thres[0])
    axis('off')
    title('Double thresholding')

    show()
