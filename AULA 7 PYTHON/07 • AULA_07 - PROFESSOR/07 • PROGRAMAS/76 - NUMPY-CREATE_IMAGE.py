from PIL import Image
import numpy as np

w, h = 512, 512
data = np.zeros((h, w, 3), dtype=np.uint8)
data[0:512, 0:512] = [255, 56, 15] # red patch in upper left
img = Image.fromarray(data, 'RGB')
img.save('my.png')
img.show()