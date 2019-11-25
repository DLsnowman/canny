import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

im_path = '/tfshare/PycharmProjects/canny/valve.png'
im = np.array(Image.open(im_path))
im = im[:, :, 0]
print(im.shape)
plt.gray()
plt.show()