import os
import numpy as np

from PIL import Image


size = 2560
lumen = 0 # 0: mirror, 1: light

img = np.ones([size, size])*lumen
img = img.astype(np.uint8)
img = Image.fromarray(img, mode='L')
img.save('./res.png')
