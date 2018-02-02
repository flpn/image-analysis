import cv2
import matplotlib.pyplot as plt
import numpy as np


image = cv2.imread('./images/watch.jpg', cv2.IMREAD_GRAYSCALE)

# manipulation with cv2
cv2.imshow('image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# manipulation with matplotlib
# plt.imshow(image, cmap='gray', interpolation='bicubic')
# plt.xticks([]), plt.yticks([])
# plt.plot([20, 30, 40], [10, 20, 30], 'c', linewidth=5)
# plt.show()

# save file manipulated file
# cv2.imwrite('new_image.jpg', image)
