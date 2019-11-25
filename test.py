import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

im_path = '/tfshare/PycharmProjects/canny/valve.png'
im = np.array(Image.open(im_path))
im = im[:, :, 0]
print(im.shape)

b = np.array([[2, 4,  5,  2,  2],
           [4, 9,  12, 9,  4],
           [5, 12, 15, 12, 5],
           [4, 9,  12, 9,  4],
           [2, 4,  5,  4,  2]]) / 156
kernel = np.zeros(im.shape)
kernel[:b.shape[0], :b.shape[1]] = b

fim = np.fft.fft2(im)
fkernel = np.fft.fft2(kernel)
fil_im = np.fft.ifft2(fim * fkernel)

fil_im = np.abs(fil_im).astype('int')

plt.gray()
plt.subplot(1, 2, 1)
plt.imshow(im)
plt.subplot(1, 2, 2)
plt.imshow(fil_im)
plt.show()