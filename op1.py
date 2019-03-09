import matplotlib.pyplot as plt
from skimage import io


img = io.imread("../data/4.jpg")
print(img.shape)

plt.imshow(img)
plt.show()
